# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(default='', max_length=40)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(max_length=2000)),
            ],
        ),
    ]
