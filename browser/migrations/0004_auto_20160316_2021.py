# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-16 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0003_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='article',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]