from rest_framework import serializers
from mentorings import models

class MentoringSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.mentorings
        fields='__all__'
        
class Mentoring_chatsSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.mentoring_chats
        fields='__all__'
        
class LocationsSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.locations
        fields='__all__'
        