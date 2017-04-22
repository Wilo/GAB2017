# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from django.forms import CheckboxSelectMultiple
from .models import Post, CategoryPost


@admin.register(CategoryPost)
class CategoriaPostAdmin(SimpleHistoryAdmin):

    fieldsets = (
        (None, {
            'fields': (
                'description',
            )
        }
        ),
    )

    search_fields = ('description',)


@admin.register(Post)
class PostAdmin(SimpleHistoryAdmin):

    fieldsets = (
        ('Nueva entrada', {
            'fields': (
                'image_tag',
                'img_header',
                'title',
                'date_creation',
                'description',
                'category',
                'status',
            ),
        }
        ),
    )

    readonly_fields = ('image_tag', )

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    list_display = (
        'slug',
        'inline_image_tag',
        'title',
        'description',
        'status',
    )

    list_filter = ('category',)

    search_fields = ('title',)

    def image_tag(self, obj):
        return "<img src={} />".format(obj.img_header.url)

    def inline_image_tag(self, obj):
        return "<img src={} width=200 height=200/>".format(obj.img_header.url)

    image_tag.short_description = "Header"
    image_tag.allow_tags = True
    inline_image_tag.short_description = "Thubnail"
    inline_image_tag.allow_tags = True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
