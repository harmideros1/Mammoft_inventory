# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20170323_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='u_hash',
            name='f_nacimiento',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 23, 19, 8, 50, 727307)),
        ),
        migrations.AlterField(
            model_name='u_hash',
            name='avatar',
            field=models.ImageField(upload_to='login/users/profile', max_length=300, default='/media/login/users/profile/none/default_avatar.png'),
        ),
    ]
