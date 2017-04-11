# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('numeracion_documentos', '0002_auto_20170410_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaproveedor',
            name='id_periodo',
            field=models.ForeignKey(to='periodos_contables.PeriodosContables', default='001', verbose_name='Periodo'),
        ),
        migrations.AlterField(
            model_name='notacredito',
            name='id_periodo',
            field=models.ForeignKey(to='periodos_contables.PeriodosContables', default='001', verbose_name='Periodo'),
        ),
        migrations.AlterField(
            model_name='notadebito',
            name='id_periodo',
            field=models.ForeignKey(to='periodos_contables.PeriodosContables', default='001', verbose_name='Periodo'),
        ),
    ]
