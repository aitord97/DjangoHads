# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-09 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tema',
            field=models.CharField(default='vacio', max_length=200),
            preserve_default=False,
        ),
    ]