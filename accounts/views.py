from .models import Members
from rest_framework import viewsets

from accounts.serializers import MembersSerializer

class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer