# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_auto_20150206_0420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='response_type',
            new_name='machine_type',
        ),
        migrations.AddField(
            model_name='response',
            name='num_machines',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
    ]
