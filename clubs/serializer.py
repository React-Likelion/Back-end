from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers


class ClubsSerializer(ModelSerializer):
    class Meta:
        model = Clubs
        fields = '__all__'

class ClubMembersSerializer(ModelSerializer):
    class Meta:
        model = ClubMembers
        fields = '__all__'

#Clubsboard_image 시리얼라이저 추가
class ClubboardImageSerializer(ModelSerializer):
    image=serializers.ImageField(use_url=True)
    
    class Meta:
        model=Clubsboard_image
        fields=['image']

class ClubBoardSerializer(ModelSerializer):
    #images필드 추가
    images=serializers.SerializerMethodField()

    class Meta:
        model = Clubboard
        fields = '__all__'
        read_only_fields = ['comment_cnt']
    
    #SerializerMethodFiled에 사용할 메소드 정의
    def get_images(self, obj):
        image=obj.clubs_image.all()
        return ClubboardImageSerializer(instance=image, many=True, context=self.context).data

    #post요청시 동작하는 메소드, view에서 생성된 Clubboard모델의 validate data에서
    #추가적으로 foreignkey로 연결된 Clubsboard_image테이블에 데이터추가
    def create(self, validated_data):
        instance = Clubboard.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        
        #post요청에서 받아온 이미지들에 대해서 각각 Clubsboard_image테이블에 create
        for image_data in image_set.getlist('image'):
            Clubsboard_image.objects.create(clubboard=instance, image=image_data)
        return instance
    


class GalleriesSerializer(ModelSerializer):
    class Meta:
        model = Galleries
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Clubboard_comment
        fields = '__all__'
