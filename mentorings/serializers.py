from rest_framework import serializers
from mentorings import models

class MentoringSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.mentorings
        fields=['user_id','location','title','description','field','age_group','limit']
        
class Mentoring_chatsSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.mentoring_chats
        fields=['user_id', 'description','create_date','mentorings_id']
        
class LocationsSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.locations
        fields='__all__'
        