# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-20 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='goods',
            new_name='product',
        ),
    ]