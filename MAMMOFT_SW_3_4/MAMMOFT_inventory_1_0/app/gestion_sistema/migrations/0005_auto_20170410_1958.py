# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_sistema', '0004_auto_20170410_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestioncontable',
            name='activos_fijos',
            field=models.BooleanField(verbose_name='Permitir activos fijos', default=False),
        ),
        migrations.AddField(
            model_name='gestioncontable',
            name='calculo_amortizado',
            field=models.CharField(verbose_name='Cálculo de amortización', max_length=100, default=''),
        ),
    ]
