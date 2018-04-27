# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-18 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpinoffParticipant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('preferredCity', models.CharField(choices=[('Bangalore', 'Bangalore'), ('Pune', 'Pune'), ('Lucknow', 'Lucknow'), ('Delhi', 'Delhi')], max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=12, unique=True)),
                ('prior_experience_if_any', models.CharField(blank=True, max_length=300, null=True)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
