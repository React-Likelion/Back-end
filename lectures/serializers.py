from rest_framework import serializers
from .models import Lectures
from accounts.models import User
from rest_framework.response import Response


class LecturesSerializer(serializers.ModelSerializer):
    
    # 강의 수강 학생 Many To Many Field
    enroll_students = serializers.SlugRelatedField(
        many=True,
        slug_field="nickname", 
        queryset = User.objects.all(),
        #write_only =True
        read_only = False
        )
    # 강의 좋아요 누른 회원 Many To Many Field
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





