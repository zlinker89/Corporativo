# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turnos', '0002_auto_20170202_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caja',
            name='IndicativoCaja',
        ),
        migrations.AddField(
            model_name='tipoturno',
            name='IndicativoTurno',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
