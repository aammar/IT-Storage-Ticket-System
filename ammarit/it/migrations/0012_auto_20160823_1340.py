# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0011_owner_imgurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemID',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemNumber',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([]),
        ),
    ]
