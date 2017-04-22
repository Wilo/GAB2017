# -*- coding: utf-8 -*-
from rest_framework import serializers
from core.post import models


class CategoryPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CategoryPost
        fields = ('url', 'pk', 'description', 'slug')


class PostSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(slug_field="description",
                                            read_only=True, many=True)

    class Meta:
        model = models.Post
        fields = ('url', 'pk', 'title', 'description',
                  'date_creation', 'img_header',
                  'category', 'status')
