# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-18 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0023_auto_20160418_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='uid',
            field=models.BigIntegerField(blank=True, default=None),
        ),
    ]