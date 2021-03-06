# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='G1File',
            fields=[
                ('unique_id', models.IntegerField(primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=100)),
                ('index', models.IntegerField()),
                ('desc', models.CharField(max_length=50)),
                ('ftype', models.CharField(max_length=20)),
                ('vdf', models.CharField(blank=True, max_length=5)),
                ('struct', models.CharField(max_length=15)),
                ('pos', models.CharField(max_length=15)),
                ('comments', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='G1PostingType',
            fields=[
                ('posting_type', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('bl', models.CharField(choices=[('B', 'B'), ('L', 'L')], max_length=1)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='G1TradeUploadErrorMessage',
            fields=[
                ('code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('posted', models.CharField(blank=True, max_length=1)),
                ('description', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
