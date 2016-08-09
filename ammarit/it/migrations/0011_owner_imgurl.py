# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0010_auto_20160803_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='imgURL',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
