# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=50)),
                ('uemail', models.CharField(max_length=30)),
                ('uaddr', models.CharField(default=b'', max_length=100)),
                ('uphone', models.CharField(default=b'', max_length=11)),
                ('upostnum', models.CharField(default=b'', max_length=6)),
            ],
        ),
    ]
