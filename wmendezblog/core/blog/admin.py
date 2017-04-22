from django.db import models
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from .models import Post, CategoriaPost


@admin.register(CategoriaPost)
class CategoriaPostAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': (
                'descripcion',
            )
        }
        ),
    )

    search_fields = ('descripcion',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Nueva entrada', {
            'fields': (
                'img_cabecera',
                'titulo',
                'fech_crea',
                'descripcion',
                'categoria',
                'estado',
            ),
        }
        ),
    )

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    list_display = (
        'slug',
        'titulo',
        'descripcion',
        'estado',
    )

    list_filter = ('categoria',)

    search_fields = ('titulo',)
