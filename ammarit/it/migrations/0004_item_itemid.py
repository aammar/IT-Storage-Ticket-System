# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0003_itemrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='itemID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
