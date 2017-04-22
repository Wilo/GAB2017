# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify


class CategoryPost(models.Model):
    description = models.CharField(max_length=140, verbose_name="Descripción")
    slug = models.SlugField(max_length=140, verbose_name="Slug Url",
                            null=True, blank=True)

    def __str__(self):
        return self.descripcition

    def save(self, *args, **kwargs):
        self.slug = slugify(self.description)
        super(CategoryPost, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Categoría de Entradas al Blog"
        verbose_name_plural = "Categorías de Entradas al Blog"
        ordering = ['-descripcion']


class Post(models.Model):
    title = models.CharField(max_length=140, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    slug = models.SlugField(max_length=140, verbose_name="Slug Url", null=True,
                            blank=True)
    date_creation = models.DateTimeField(default=datetime.now,
                                         verbose_name="Fecha de Creación")
    img_header = models.ImageField(upload_to='post', null=True,
                                   verbose_name="Cabecera")
    category = models.ManyToManyField(CategoryPost, verbose_name="Categoría")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.fech_crea = datetime.now()
        self.slug = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Entrada al Blog"
        verbose_name_plural = "Entradas al Blog"
        ordering = ['-date_creation']
