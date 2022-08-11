from urllib import request
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView

from .serializers import CommunitySerializers, CommunityCommentsSerializers
from .models import Community, CommunityComments

class CommunityViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Community.objects.all()
    serializer_class = CommunitySerializers


class CommunityCommentsViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = CommunityComments.objects.all()
    serializer_class = CommunityCommentsSerializers

    def perform_create(self, serializer):
        print(self.request.board_id)
        #cnt = Community.objects.get(id = pk)
        #print(cnt)
        #cnt.comment_cnt += 1
        #scnt.save()
        return super().perform_create(serializer)

    
