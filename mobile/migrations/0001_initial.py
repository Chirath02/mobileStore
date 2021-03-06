# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=300)),
                ('brand_name', models.CharField(max_length=300)),
                ('battery_capacity', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('front_cam', models.FloatField()),
                ('back_cam', models.FloatField()),
                ('ram', models.FloatField()),
                ('screen_size', models.FloatField()),
                ('price', models.FloatField()),
                ('release_data', models.DateTimeField()),
                ('img', models.ImageField(upload_to='/mobile/')),
            ],
        ),
    ]
