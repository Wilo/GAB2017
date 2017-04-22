# -*- coding: utf-8 -*-

from django_filters import CharFilter, FilterSet
from core.post.models import Post


class PostFilter(FilterSet):
    slug = CharFilter(name="Post")
    category = CharFilter(name="category__description")
    date = CharFilter(name="date_creation")

    class Meta:
        model = Post
        fields = ('slug', 'category', 'date', )
