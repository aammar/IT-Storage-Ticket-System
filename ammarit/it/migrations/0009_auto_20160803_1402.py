# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0008_item_imgurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='imgURL',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
