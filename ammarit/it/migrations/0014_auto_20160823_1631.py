# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0013_auto_20160823_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('itemNumber', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='itemrequest',
            name='itemNumber',
        ),
        migrations.AddField(
            model_name='itemrequest',
            name='desc',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requesteditem',
            name='request',
            field=models.ForeignKey(to='it.ItemRequest'),
        ),
    ]
