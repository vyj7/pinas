# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-20 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flupld', '0002_auto_20160318_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedata',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
