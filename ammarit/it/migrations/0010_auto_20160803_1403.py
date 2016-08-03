# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0009_auto_20160803_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(blank=True, to='it.Owner', null=True),
        ),
    ]
