# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-23 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='adınız')),
                ('surname', models.CharField(max_length=120, verbose_name='Soyadınız')),
                ('recorded_date', models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')),
            ],
            options={
                'ordering': ['-recorded_date', 'id'],
            },
        ),
    ]
