# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-16 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0005_auto_20160316_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
