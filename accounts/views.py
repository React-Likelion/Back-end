import traceback
from .models import User
from .tokens import account_activation_token
from .serializers import SignupSerializer, LoginSerializer

from rest_framework import status, generics, views, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse
from django.shortcuts import redirect


class UserListView(generics.ListAPIView):
    permission_classes = [AllowAny,]

    queryset = User.objects.all()
    serializer_class = SignupSerializer

class SignupView(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    queryset = User.objects.all()

    serializer_class = SignupSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            
            # jwt 토큰 => 쿠키에 저장
            res.set_cookie("access_token", access_token, httponly=True)
            res.set_cookie("refresh_token", refresh_token, httponly=True)
            
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserActivate(views.APIView):
    permission_classes = [AllowAny,]

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        try:
            if user is not None and account_activation_token.check_token(user, token):
               user.is_active = True
               user.save()
               return redirect("http://localhost:3000/login")
            else:
               return HttpResponse('만료된 링크입니다', status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(traceback.format_exc(e))

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny,]
    
    # Login
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        token = serializer.validated_data
        return Response({"token":token}, status=status.HTTP_200_OK)
   
    # Logout
    def delete(self, request):
        response = Response({"message": "Logout success"}, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response

""" class PointViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PointSerializer
 """