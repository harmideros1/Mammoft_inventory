# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20170323_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile',
        ),
        migrations.AddField(
            model_name='u_hash',
            name='avatar',
            field=models.ImageField(upload_to='login/users/profile', default='login/users/profile/none/default_avatar.png'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
