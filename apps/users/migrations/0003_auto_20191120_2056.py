# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-20 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191120_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryaddress',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.UserInfo'),
        ),
    ]
