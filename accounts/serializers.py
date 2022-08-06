from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class MembersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
 
class LoginSerializer(serializers.ModelSerializer):
    identification = serializers.CharField(
        required = True,
        write_only = True
    )
    password = serializers.CharField(
        required = True,
        write_only = True,
        style= {'input_type' : 'password'}
    )
    class Meta(object):
        model = User
        fields = ('identification', 'password')

    def validate(self, data):
        identification = data.get('identification',None)
        password = data.get('password',None)

        if User.objects.filter(identification=identification).exists():
            user = User.objects.get(identification=identification)
            if user.check_password(password):
                raise serializers.ValidationError('Check Your Identification or Password')
        
        else:
            raise serializers.ValidationError("User does not exist")
        

        token = RefreshToken.for_user(user=user)
        data = {
            'user' : user.id,
            'refresh_token' : str(token),
            'access_token' : str(token.access_token)
        }
        return data