from .models import Members
from rest_framework import viewsets
from rest_framework import status, generics
from rest_framework.response import Response
from accounts.serializers import MembersSerializer, LoginSerializer
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
#from rest_framework.permissions import IsAuthenticated

class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

    #permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=False):
            user = serializer.save(request)

            token = RefreshToken.for_user(user)
            refresh = str(token)
            access = str(token.access_token)

            return JsonResponse({'user': user, 'access': access, 'refresh': refresh})
 
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception = True)
        token = serializer.validated_data
        return Response({"token":token}, status=status.HTTP_200_OK)