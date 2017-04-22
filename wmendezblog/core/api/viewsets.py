# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.filters import DjangoFilterBackend
from rest_framework import permissions

from .filters import PostFilter
from .serializers import CategoryPostSerializer, PostSerializer

from core.post import models


class CategoryPostViewSet(viewsets.ModelViewSet):
    queryset = models.CategoryPost.objects.all()
    serializer_class = CategoryPostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.filter(status=True)
    serializer_class = PostSerializer
    filter_backend = DjangoFilterBackend
    filter_class = PostFilter
    permission_classes = (permissions.IsAuthenticated,)
