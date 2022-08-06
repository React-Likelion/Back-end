import traceback
from .models import Members
from .tokens import account_activation_token

from rest_framework import status, generics, views, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import SignupSerializer, LoginSerializer

from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse

class MembersListView(generics.ListAPIView):
    queryset = Members.objects.all()
    serializer_class = SignupSerializer

class SignupView(generics.CreateAPIView):
    queryset = Members.objects.all()
    serializer_class = SignupSerializer
    def post(self, request):
      serializer = self.get_serializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserActivate(views.APIView):
    permission_classes = [AllowAny,]

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = Members.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, Members.DoesNotExist):
            user = None

        try:
            if user is not None and account_activation_token.check_token(user, token):
               user.is_active = True
               user.save()
               return HttpResponse(user.email + '계정이 활성화 되었습니다', status=status.HTTP_200_OK)
            else:
               return HttpResponse('만료된 링크입니다', status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(traceback.format_exc())

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception = True)
        token = serializer.validated_data
        return Response({"token":token}, status=status.HTTP_200_OK)