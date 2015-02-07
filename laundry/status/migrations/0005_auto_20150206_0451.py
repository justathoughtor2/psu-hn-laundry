# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0004_auto_20150206_0445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='in_use',
        ),
        migrations.RemoveField(
            model_name='response',
            name='num_machines',
        ),
        migrations.AddField(
            model_name='response',
            name='machine_in_use',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
    ]
