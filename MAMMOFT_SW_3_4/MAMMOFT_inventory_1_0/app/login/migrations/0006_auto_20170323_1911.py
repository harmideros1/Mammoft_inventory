# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20170323_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='u_hash',
            name='f_nacimiento',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
