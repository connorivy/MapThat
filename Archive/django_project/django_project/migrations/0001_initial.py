# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 21:01
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='spots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to=b'')),
                ('geom', djgeojson.fields.PolygonField()),
            ],
        ),
    ]