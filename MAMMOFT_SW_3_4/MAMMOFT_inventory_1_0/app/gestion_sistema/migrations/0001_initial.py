# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sociedad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=300, default='')),
                ('direccion', models.CharField(max_length=300, default='')),
                ('apartado', models.CharField(max_length=300, default='')),
                ('calle', models.CharField(max_length=300, default='')),
                ('ciudad', models.CharField(max_length=300, default='')),
                ('condado', models.CharField(max_length=300, default='')),
                ('codigo_postal', models.CharField(max_length=10, default='')),
                ('estado', models.CharField(max_length=300, default='')),
                ('pais', models.CharField(max_length=300, default='')),
                ('web', models.CharField(max_length=500, default='')),
                ('telefono_uno', models.CharField(max_length=20, default='')),
                ('telefono_dos', models.CharField(max_length=20, default='')),
                ('correo', models.EmailField(max_length=254, help_text='Ingresa un correo válido por favor.', default='')),
            ],
        ),
    ]
