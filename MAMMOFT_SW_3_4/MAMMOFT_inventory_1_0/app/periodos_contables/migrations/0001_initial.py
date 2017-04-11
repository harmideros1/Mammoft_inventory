# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodosContables',
            fields=[
                ('codigo_periodo', models.CharField(default='', primary_key=True, verbose_name='Código de periodo', max_length=300, serialize=False)),
                ('nombre_periodo', models.CharField(default='', verbose_name='Nombre', max_length=300)),
                ('subperiodos', models.CharField(default='', max_length=60, choices=[('periodo1', 'periodo1'), ('periodo2', 'periodo2')])),
                ('fecha_contabilizacion', models.DateTimeField()),
                ('fecha_vencimiento', models.DateTimeField()),
                ('fecha_documento', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Periodos',
            },
        ),
    ]
