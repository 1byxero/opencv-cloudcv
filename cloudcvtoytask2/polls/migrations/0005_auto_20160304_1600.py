# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-04 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20160304_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='foregroundextract',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='document',
            name='sobelfilter',
            field=models.BooleanField(default=False),
        ),
    ]
