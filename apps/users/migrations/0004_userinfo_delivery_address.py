# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-20 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191120_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='delivery_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_delivery_address', to='users.DeliveryAddress'),
        ),
    ]
