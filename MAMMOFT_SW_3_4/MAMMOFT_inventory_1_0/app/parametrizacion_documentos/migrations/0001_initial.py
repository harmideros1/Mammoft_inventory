# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParametrizacionDocumentos',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('calculo_ingreso_bruto', models.CharField(verbose_name='Cálculo ingreso bruto', max_length=300, choices=[('dato1', 'dato1'), ('dato2', 'dato2')], default='')),
                ('calculo_ganancia_ruta', models.CharField(verbose_name='Cálculo ganancia ruta', max_length=300, choices=[('dato1', 'dato1'), ('dato2', 'dato2')], default='')),
                ('bloqueo_stock_negativos', models.CharField(verbose_name='Bloqueo stock negativos', max_length=300, choices=[('dato1', 'dato1'), ('dato2', 'dato2')], default='')),
            ],
            options={
                'verbose_name_plural': 'Parametrización Documentos',
            },
        ),
    ]
