# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-24 19:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0006_auto_20171219_1854'),
    ]

    operations = [
        migrations.DeleteModel(
            name='employees',
        ),
    ]