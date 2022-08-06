from mentorings import models, serializers
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

#멘토링 CRUD
class MentoringViewSet(viewsets.ModelViewSet):
    queryset=models.mentorings.objects.all()
    serializer_class=serializers.MentoringSerializers
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['title', 'age_group', 'location', 'field']

#멘토링 챗 CRUD    
class Mentoring_ChatsViewSet(viewsets.ModelViewSet):
    queryset=models.mentoring_chats.objects.all()
    serializer_class=serializers.Mentoring_chatsSerializers 

#foreign-key검색 여부확인 용 임시 viewset
class Locations_ViewSet(viewsets.ModelViewSet):
    queryset=models.locations.objects.all()
    serializer_class=serializers.LocationsSerializers 
    
