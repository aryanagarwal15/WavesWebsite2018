# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-09 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spinoff', '0003_auto_20170622_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spinoffparticipant',
            name='preferredCity',
            field=models.CharField(choices=[('Goa', 'Goa'), ('Bangalore', 'Bangalore'), ('Pune', 'Pune'), ('Mumbai', 'Mumbai'), ('Delhi', 'Delhi')], max_length=20),
        ),
    ]
