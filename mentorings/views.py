from mentorings import models, serializers
from rest_framework import viewsets

class MentoringViewSet(viewsets.ModelViewSet):
    queryset=models.mentorings.objects.all()
    serializer_class=serializers.MentoringSerializers
    
class Mentoring_ChatsViewSet(viewsets.ModelViewSet):
    queryset=models.mentoring_chats.objects.all()
    serializer_class=serializers.Mentoring_chatsSerializers    