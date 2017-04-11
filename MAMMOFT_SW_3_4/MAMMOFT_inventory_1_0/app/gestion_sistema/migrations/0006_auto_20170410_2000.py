# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_sistema', '0005_auto_20170410_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestioncontable',
            name='activos_fijos',
            field=models.BooleanField(verbose_name='Permitir activos fijos'),
        ),
    ]
