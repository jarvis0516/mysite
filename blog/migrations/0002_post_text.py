# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=None),
        ),
    ]
