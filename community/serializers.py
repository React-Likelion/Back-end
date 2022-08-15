from rest_framework import serializers
from .models import Community, CommunityComments

class CommunitySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Community
        fields = '__all__'

class CommunityCommentsSerializers(serializers.ModelSerializer):

    class Meta:
        model = CommunityComments
        fields = '__all__'
    
    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many = True)
        serializer.bind('', self)
        return serializer.data

class CommunityOnlySerializers(serializers.ModelSerializer):
    parent_comments = serializers.SerializerMethodField()

    class Meta:
        model = Community
        fields = ['id', 'parent_comments']
    
    def get_parent_comments(self, obj):
        parent_comments = obj.comment.filter(comment_id = None)
        serializer = CommunityCommentsSerializers(parent_comments, many = True)
        return serializer.data

class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['id', 'title', 'category', 'writer_id']
