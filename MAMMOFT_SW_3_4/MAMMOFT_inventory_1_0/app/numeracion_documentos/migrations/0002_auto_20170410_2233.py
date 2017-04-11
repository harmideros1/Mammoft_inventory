# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('periodos_contables', '0001_initial'),
        ('numeracion_documentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturaclientes',
            name='id_periodo',
            field=models.ForeignKey(to='periodos_contables.PeriodosContables', default='001'),
        ),
        migrations.AddField(
            model_name='facturaproveedor',
            name='id_periodo',
            field=models.ForeignKey(to='periodos_contables.PeriodosContables', default='001'),
        ),
        migrations.AddField(
            model_name='notacredito',
            name='id_periodo',
            field=models.ForeignKey(to='periodos_contables.PeriodosContables', default='001'),
        ),
        migrations.AddField(
            model_name='notadebito',
            name='id_periodo',
            field=models.ForeignKey(to='periodos_contables.PeriodosContables', default='001'),
        ),
    ]
