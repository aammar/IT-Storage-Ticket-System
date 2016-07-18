# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Item_Number',
            new_name='itemNumber',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Make',
            new_name='make',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Model',
            new_name='model',
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(to='it.Owner', null=True),
        ),
    ]
