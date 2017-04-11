# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20170323_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='u_hash',
            name='cargo',
            field=models.CharField(default='Sin cargo', max_length=100),
        ),
        migrations.AddField(
            model_name='u_hash',
            name='direccion',
            field=models.CharField(default='Sin dirección', max_length=200),
        ),
        migrations.AddField(
            model_name='u_hash',
            name='sexo',
            field=models.CharField(default='No definido', max_length=15),
        ),
    ]
