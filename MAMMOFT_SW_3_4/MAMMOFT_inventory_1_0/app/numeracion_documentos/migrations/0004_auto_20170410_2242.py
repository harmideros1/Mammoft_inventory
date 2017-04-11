# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('numeracion_documentos', '0003_auto_20170410_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaclientes',
            name='id_periodo',
            field=models.ForeignKey(default='001', verbose_name='Periodo', to='periodos_contables.PeriodosContables'),
        ),
    ]
