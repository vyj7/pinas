# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-17 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0010_auto_20160317_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
