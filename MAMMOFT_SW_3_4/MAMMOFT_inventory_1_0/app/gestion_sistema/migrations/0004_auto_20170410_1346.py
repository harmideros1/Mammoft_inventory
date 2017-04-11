# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_sistema', '0003_auto_20170410_1314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gestioncontable',
            options={'verbose_name_plural': 'Gestión Contable'},
        ),
        migrations.AlterField(
            model_name='gestioncontable',
            name='ciu_consignacion',
            field=models.CharField(verbose_name='Ciudad de consignación', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='gestioncontable',
            name='hacienda',
            field=models.CharField(verbose_name='Hacienda', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='gestioncontable',
            name='ide_fiscal_nit',
            field=models.CharField(verbose_name='Identificación Fiscal / Nit', default='', max_length=100),
        ),
    ]
