import traceback
from .models import User
from .tokens import account_activation_token
from .serializers import SignupSerializer, LoginSerializer, UserSerializer, PointSerializer, UserPointSerializer, UserDetailSerializer

from rest_framework import status, generics, views, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import action

from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse
from django.shortcuts import redirect

# 회원 목록 view
class UserListView(generics.ListAPIView):
    permission_classes = [AllowAny,]

    queryset = User.objects.all()
    serializer_class = SignupSerializer

# 회원가입 view
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

# 회원정보 활성화
class UserActivate(views.APIView):
    permission_classes = [AllowAny,]

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))  # 암호화하였던 user의 id를 다시 decode 함으로써 해당 user 불러옴
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        try:
            if user is not None and account_activation_token.check_token(user, token):  # check_token으로 유효성 검사
               # 해당 user가 존재하고 token도 유효하다면 active를 활성화 해주고 로그인 페이지로 이동
               user.is_active = True
               user.save()
               return redirect("http://localhost:3000/login")
            else:
               return HttpResponse('만료된 링크입니다', status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:  # 예외 발생 시
            print(traceback.format_exc(e))

# 로그인 & 로그아웃 view
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
        # cookie에서 access, refresh 토큰 삭제하여 로그아웃
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response


class PointViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PointSerializer

class UserPointView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserPointSerializer

# 회원정보 수정 view
class UserUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def patch(self, request, pk):
        serializer = self.get_serializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = Response(
                {
                    "user": serializer.data,
                    "message": "update successs",
                },
                status=status.HTTP_200_OK,
            )
            
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 회원 상세페이지 ViewSet
class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    permission_classes = [AllowAny,]

    @action(detail=True)
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

user_detail = UserDetailViewSet.as_view({
    'get': 'retrieve',
    'patch' : 'partial_update'
})
