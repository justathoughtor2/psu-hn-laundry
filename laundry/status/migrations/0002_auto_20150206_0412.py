# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='available',
        ),
        migrations.RemoveField(
            model_name='response',
            name='response_text',
        ),
        migrations.AddField(
            model_name='response',
            name='response_value',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
