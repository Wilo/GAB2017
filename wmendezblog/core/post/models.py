# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.template.defaultfilters import slugify
from simple_history.models import HistoricalRecords


class CategoryPost(models.Model):
    description = models.CharField(max_length=140, verbose_name="Descripción")
    slug = models.SlugField(max_length=140, verbose_name="Slug Url",
                            null=True, blank=True)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('search', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.description)
        super(CategoryPost, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Categoría de Entradas al Blog"
        verbose_name_plural = "Categorías de Entradas al Blog"
        ordering = ['-description']


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=140, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    slug = models.SlugField(max_length=140, verbose_name="Slug Url", null=True,
                            blank=True)
    date_creation = models.DateTimeField(default=datetime.now,
                                         verbose_name="Fecha de Creación")
    img_header = models.ImageField(upload_to='post', null=True,
                                   verbose_name="Cabecera")
    category = models.ManyToManyField(CategoryPost, verbose_name="Categoría")
    status = models.BooleanField(default=False, verbose_name="¿Publicado?")

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.title

    def post_length(self):
        return len(self.img_header.name)

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.fech_crea = datetime.now()
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Entrada al Blog "
        verbose_name_plural = "Entradas al Blog "
        ordering = ['-date_creation']
