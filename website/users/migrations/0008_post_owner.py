# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20170403_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
