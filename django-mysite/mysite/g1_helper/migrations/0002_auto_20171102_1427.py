# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g1_helper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g1file',
            name='unique_id',
            field=models.CharField(max_length=150, primary_key=True, serialize=False),
        ),
    ]
