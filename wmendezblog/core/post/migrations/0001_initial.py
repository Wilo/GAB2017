# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 02:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=140, verbose_name='Descripción')),
                ('slug', models.SlugField(blank=True, max_length=140, null=True, verbose_name='Slug Url')),
            ],
            options={
                'verbose_name': 'Categoría de Entradas al Blog',
                'verbose_name_plural': 'Categorías de Entradas al Blog',
                'ordering': ['-description'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('slug', models.SlugField(blank=True, max_length=140, null=True, verbose_name='Slug Url')),
                ('date_creation', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de Creación')),
                ('img_header', models.ImageField(null=True, upload_to='post', verbose_name='Cabecera')),
                ('status', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='post.CategoryPost', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Entrada al Blog',
                'verbose_name_plural': 'Entradas al Blog',
                'ordering': ['-date_creation'],
            },
        ),
    ]
