# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-25 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_tickets_tickets_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='tickets_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
