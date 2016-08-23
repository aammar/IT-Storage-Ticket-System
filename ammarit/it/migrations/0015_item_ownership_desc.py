# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0014_auto_20160823_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ownership_desc',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
