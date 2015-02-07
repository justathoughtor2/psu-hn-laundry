# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20150206_0412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='response_value',
            new_name='in_use',
        ),
        migrations.AddField(
            model_name='response',
            name='response_type',
            field=models.CharField(default='Laundry Machine', max_length=200),
            preserve_default=False,
        ),
    ]
