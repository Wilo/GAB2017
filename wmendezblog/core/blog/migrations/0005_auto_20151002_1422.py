# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151002_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriapost',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug Url', max_length=140),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Slug Url', max_length=140),
        ),
    ]
