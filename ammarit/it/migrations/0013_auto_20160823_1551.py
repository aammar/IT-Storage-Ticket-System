# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0012_auto_20160823_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemrequest',
            name='item',
        ),
        migrations.AddField(
            model_name='itemrequest',
            name='itemNumber',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
