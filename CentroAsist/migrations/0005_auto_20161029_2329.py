# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-29 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CentroAsist', '0004_auto_20161029_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrohc',
            old_name='registro_paciente',
            new_name='paciente',
        ),
        migrations.AlterField(
            model_name='registrohc',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
