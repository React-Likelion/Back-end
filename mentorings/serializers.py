from rest_framework import serializers
from mentorings import models

class MentoringSerializers(serializers.ModelSerializer):
    image=serializers.ImageField(use_url=True)
    class Meta:
        model=models.mentorings
        fields=['user_id','location','title','description','field','age_group','limit','nickname','member_cnt','image']
        
class Mentoring_chatsSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.mentoring_chats
        fields=['user_id', 'description','create_date','mentorings_id','nickname']
        
class LocationsSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.locations
        fields='__all__'
        