# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-17 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0016_auto_20160320_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='roll_no',
        ),
        migrations.AddField(
            model_name='signup',
            name='auth',
            field=models.BooleanField(default=False),
        ),
    ]