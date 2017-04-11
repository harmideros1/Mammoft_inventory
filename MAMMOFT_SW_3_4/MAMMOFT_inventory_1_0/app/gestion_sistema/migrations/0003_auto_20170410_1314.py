# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_sistema', '0002_gestion_contable'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gestion_Contable',
            new_name='GestionContable',
        ),
        migrations.AlterModelOptions(
            name='gestioncontable',
            options={'verbose_name_plural': 'Gestion Contable'},
        ),
        migrations.AlterModelOptions(
            name='sociedad',
            options={'verbose_name_plural': 'Sociedad'},
        ),
    ]
