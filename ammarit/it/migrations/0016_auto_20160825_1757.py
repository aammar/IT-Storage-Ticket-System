# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0015_item_ownership_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logText', models.CharField(max_length=2000)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='ownership_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 25, 17, 57, 48, 111880, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
