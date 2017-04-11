# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20170323_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='u_hash',
            name='edad',
            field=models.CharField(max_length=3, default='0'),
        ),
    ]
