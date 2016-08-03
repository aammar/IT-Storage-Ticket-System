# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0007_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='imgURL',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
