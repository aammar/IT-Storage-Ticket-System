# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0002_auto_20160718_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(to='it.Item')),
                ('requester', models.ForeignKey(to='it.Owner')),
            ],
        ),
    ]
