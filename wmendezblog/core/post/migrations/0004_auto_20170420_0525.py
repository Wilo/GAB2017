# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-20 05:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_historicalcategorypost_historicalpost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalpost',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Entrada al Blog '},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_creation'], 'verbose_name': 'Entrada al Blog ', 'verbose_name_plural': 'Entradas al Blog '},
        ),
    ]
