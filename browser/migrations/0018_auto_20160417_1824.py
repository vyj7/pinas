# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-17 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0017_auto_20160417_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='auth',
            field=models.BooleanField(),
        ),
    ]
