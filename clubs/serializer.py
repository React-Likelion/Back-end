from rest_framework.serializers import ModelSerializer
from .models import *


class ClubsSerializer(ModelSerializer):
    class Meta:
        model = Clubs
        fields = '__all__'
