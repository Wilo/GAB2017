# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaPost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('descripcion', models.CharField(max_length=140, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('titulo', models.CharField(max_length=140, verbose_name='Título')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('fech_crea', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de Creación')),
                ('estado', models.BooleanField(default=False)),
                ('categoria', models.ManyToManyField(verbose_name='Categoría', to='blog.CategoriaPost')),
            ],
        ),
    ]
