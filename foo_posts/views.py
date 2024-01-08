from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

# Create your views here.
class FooPostViewSet (viewsets.ModelViewSet):
    queryset = FooPost.objects.all()
    serializer_class = FooPostSerializer
    permission_classes = [IsAuthenticated,]

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user

        post.like_post(user)
        post_serializer = FooPostSerializer(post)
        return Response(post_serializer.data)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user

        post.unlike_post(user)
        post_serializer = FooPostSerializer(post)
        return Response(post_serializer.data)