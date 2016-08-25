# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0018_log_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='subtext',
            field=models.CharField(default='', max_length=10000),
            preserve_default=False,
        ),
    ]
