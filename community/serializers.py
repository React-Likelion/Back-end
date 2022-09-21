from rest_framework import serializers
from .models import Community, CommunityComments, Community_Image

#이미지 serializer추가
class CommunityImageSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(use_url=True)
    
    class Meta:
        model=Community_Image
        fields=['image']

class CommunitySerializers(serializers.ModelSerializer):
    images=serializers.SerializerMethodField()    
    
    class Meta:
        model = Community
        fields = '__all__'
        
    def get_images(self, obj):
        image=obj.community_image.all()
        return CommunityImageSerializer(instance=image, many=True, context=self.context).data

    def create(self, validated_data):
        instance = Community.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        
        #post요청에서 받아온 이미지들에 대해서 각각 Clubsboard_image테이블에 create
        for image_data in image_set.getlist('image'):
            Community_Image.objects.create(community=instance, image=image_data)
        return instance

class CommunityCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommunityComments
        fields = '__all__'
    
    # 대댓글 형식으로 묶어줌
    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many = True)
        serializer.bind('', self)
        return serializer.data

""" class CommunityOnlySerializers(serializers.ModelSerializer):
    parent_comments = serializers.SerializerMethodField()

    class Meta:
        model = Community
        fields = ['id', 'parent_comments']
    
    def get_parent_comments(self, obj):
        parent_comments = obj.comment.filter(comment_id = None)
        serializer = CommunityCommentsSerializers(parent_comments, many = True)
        return serializer.data """

