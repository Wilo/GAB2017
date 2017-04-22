# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150929_1431'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriapost',
            options={'verbose_name_plural': 'Categorías de Entradas al Blog', 'verbose_name': 'Categoría de Entradas al Blog', 'ordering': ['-descripcion']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Entradas al Blog', 'verbose_name': 'Entrada al Blog', 'ordering': ['-fech_crea']},
        ),
    ]
