from .models import User, Logs
from .tokens import account_activation_token
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate

class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
    ),
    password = serializers.CharField(
        required=True,
        write_only = True,
    )
    password2 = serializers.CharField(write_only = True, required=True)
    
    class Meta:
        model = User
        fields = '__all__'
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                "password" : "Password fields didn't match"
            })
        
        return data

    def create(self, validated_data):
        user = User.objects.create(
            identification = validated_data['identification'],
            name = validated_data['name'],
            nickname = validated_data['nickname'],
            email = validated_data['email'],
            birth = validated_data['birth'],
            job = validated_data['job'],
        )
        token = RefreshToken.for_user(user)
        user.set_password(validated_data['password'])
        user.refreshtoken = token
        user.is_active = False
        user.save()

        message = render_to_string('account_activate_email.html', {
          'user': user,
          'domain': 'https://port-0-back-end-14q6cqs24l6kns2t6.gksl1.cloudtype.app',
          'uid': urlsafe_base64_encode(force_bytes(user.pk)),
          'token': account_activation_token.make_token(user),
        })


        mail_subject = 'Re:act 계정을 활성화 해주세요'
        to_email = validated_data['email']
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
    
        return user

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
        
        user = authenticate(**data)
        if user and user.is_active:   # 이메일 인증 후 로그인 가능
            if User.objects.filter(identification=identification).exists():
                user = User.objects.get(identification=identification)
                update_last_login(None, user) ##last_login update

                if not user.check_password(password):
                    raise serializers.ValidationError('아이디 또는 비밀번호를 확인해주세요.')
        
            else:
                raise serializers.ValidationError("회원정보가 일치하지 않습니다.")
        
            token = RefreshToken.for_user(user=user)
            data = {
                'user' : user.id, 
                'email' : user.email,
                'nickname' : user.nickname,
                "message": "login successs",
                'refresh_token' : str(token),
                'access_token' : str(token.access_token)
            }   
            return data
        raise serializers.ValidationError("계정이 활성화 전입니다. 계정을 활성화하세요.")


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = '__all__'

class PointSerializer(serializers.ModelSerializer):
    serializer = LogSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'nickname', 'point', 'log')

class UserPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'nickname', 'point')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=True,
        write_only = True,
    )

    password2 = serializers.CharField(write_only = True, required=True)
    
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('email','point',)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                "password" : "Password fields didn't match"
            })
        
        return data

