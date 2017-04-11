# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaClientes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('primer_numero', models.IntegerField(default='0', verbose_name='Primer Número')),
                ('suiguiente_numero', models.IntegerField(default='1', verbose_name='Siguiente Número')),
                ('ultimo_numero', models.IntegerField(default='99999', verbose_name='Último Número')),
                ('prefijo', models.CharField(max_length=300, default='', verbose_name='Prefijo')),
                ('sufijo', models.CharField(max_length=300, default='', verbose_name='Sufijo')),
                ('comentario', models.CharField(max_length=300, default='', verbose_name='Comentario')),
                ('cancelacion', models.BooleanField(default=False, verbose_name='Cancelación')),
                ('bloqueo', models.BooleanField(default=False, verbose_name='Bloqueo')),
            ],
            options={
                'verbose_name_plural': 'Facura Clientes',
            },
        ),
        migrations.CreateModel(
            name='FacturaProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('primer_numero', models.IntegerField(default='0', verbose_name='Primer Número')),
                ('suiguiente_numero', models.IntegerField(default='1', verbose_name='Siguiente Número')),
                ('ultimo_numero', models.IntegerField(default='99999', verbose_name='Último Número')),
                ('prefijo', models.CharField(max_length=300, default='', verbose_name='Prefijo')),
                ('sufijo', models.CharField(max_length=300, default='', verbose_name='Sufijo')),
                ('comentario', models.CharField(max_length=300, default='', verbose_name='Comentario')),
                ('cancelacion', models.BooleanField(default=False, verbose_name='Cancelación')),
                ('bloqueo', models.BooleanField(default=False, verbose_name='Bloqueo')),
            ],
            options={
                'verbose_name_plural': 'Facura Proveedor',
            },
        ),
        migrations.CreateModel(
            name='NotaCredito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('primer_numero', models.IntegerField(default='0', verbose_name='Primer Número')),
                ('suiguiente_numero', models.IntegerField(default='1', verbose_name='Siguiente Número')),
                ('ultimo_numero', models.IntegerField(default='99999', verbose_name='Último Número')),
                ('prefijo', models.CharField(max_length=300, default='', verbose_name='Prefijo')),
                ('sufijo', models.CharField(max_length=300, default='', verbose_name='Sufijo')),
                ('comentario', models.CharField(max_length=300, default='', verbose_name='Comentario')),
                ('cancelacion', models.BooleanField(default=False, verbose_name='Cancelación')),
                ('bloqueo', models.BooleanField(default=False, verbose_name='Bloqueo')),
            ],
            options={
                'verbose_name_plural': 'Nota Crédito',
            },
        ),
        migrations.CreateModel(
            name='NotaDebito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('primer_numero', models.IntegerField(default='0', verbose_name='Primer Número')),
                ('suiguiente_numero', models.IntegerField(default='1', verbose_name='Siguiente Número')),
                ('ultimo_numero', models.IntegerField(default='99999', verbose_name='Último Número')),
                ('prefijo', models.CharField(max_length=300, default='', verbose_name='Prefijo')),
                ('sufijo', models.CharField(max_length=300, default='', verbose_name='Sufijo')),
                ('comentario', models.CharField(max_length=300, default='', verbose_name='Comentario')),
                ('cancelacion', models.BooleanField(default=False, verbose_name='Cancelación')),
                ('bloqueo', models.BooleanField(default=False, verbose_name='Bloqueo')),
            ],
            options={
                'verbose_name_plural': 'Nota Débito',
            },
        ),
    ]
