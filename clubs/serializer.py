from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import *


class ClubsSerializer(ModelSerializer):
    class Meta:
        model = Clubs
        fields = '__all__'


class ClubBoardSerializer(ModelSerializer):
    class Meta:
        model = Clubboard
        fields = '__all__'
        read_only_fields = ['comment_cnt']
