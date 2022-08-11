from rest_framework import serializers
from .models import Lectures
from accounts.models import User
from rest_framework.response import Response


class LecturesSerializer(serializers.ModelSerializer):
    
    enroll_students = serializers.SlugRelatedField(
        many=True,
        slug_field="nickname", 
        queryset = User.objects.all(),
        #write_only =True
        read_only = False
        )
    
    like_members = serializers.SlugRelatedField(
        many=True,
        slug_field="nickname", 
        queryset = User.objects.all(),
        #write_only =True
        read_only = False
        )

    class Meta:
        model = Lectures
        #fields = ['id', 'title', 'description', 'price', 'youtube_link', 'main_category', 'sub_category', 'writer', 'enroll_students', 'enroll_cnt', 'like_members', 'like_cnt', 'visit_cnt', 'create_date', 'writer', 'images']
        fields = '__all__'

    
