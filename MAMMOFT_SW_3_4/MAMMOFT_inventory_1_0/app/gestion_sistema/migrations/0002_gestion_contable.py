# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gestion_Contable',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('ide_fiscal_nit', models.CharField(max_length=100, default='')),
                ('hacienda', models.CharField(max_length=100, default='')),
                ('ciu_consignacion', models.CharField(max_length=100, default='')),
            ],
        ),
    ]
