# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-28 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_auto_20170528_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamemap',
            name='votes',
            field=models.IntegerField(default=1),
        ),
    ]