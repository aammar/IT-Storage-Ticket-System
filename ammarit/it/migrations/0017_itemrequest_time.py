# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0016_auto_20160825_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemrequest',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 25, 17, 59, 25, 545125, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
