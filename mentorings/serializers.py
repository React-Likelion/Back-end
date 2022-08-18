from dataclasses import field
from rest_framework import serializers
from mentorings import models

class MentoringSerializers(serializers.ModelSerializer):
    image=serializers.ImageField(use_url=True)
    User=serializers.SlugRelatedField(
        many=True, 
        read_only=True,
        slug_field='nickname'
        )
    class Meta:
        model=models.mentorings
        exclude=['member_cnt']


class Mentoring_chatsSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.mentoring_chats
        fields=['user_id', 'description', 'create_date', 'mentorings_id','nickname']
        
        
