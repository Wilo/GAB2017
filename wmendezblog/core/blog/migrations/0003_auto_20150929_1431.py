# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_img_cabecera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_cabecera',
            field=models.ImageField(upload_to='post', verbose_name='Cabecera', null=True),
        ),
    ]
