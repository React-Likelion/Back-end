from .models import Members
from rest_framework import serializers

class MembersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'