from .models import Members
from rest_framework import viewsets
from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import SignupSerializer, LoginSerializer
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
#from rest_framework.permissions import IsAuthenticated

class SignupView(generics.CreateAPIView):
    queryset = Members.objects.all()
    serializer_class = SignupSerializer

    #permission_classes = []
    
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception = True)
        token = serializer.validated_data
        return Response({"token":token}, status=status.HTTP_200_OK)