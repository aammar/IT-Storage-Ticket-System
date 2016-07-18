# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('Item_Number', models.IntegerField(serialize=False, primary_key=True)),
                ('Category', models.CharField(max_length=200)),
                ('Make', models.CharField(max_length=200)),
                ('Model', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FName', models.CharField(max_length=200)),
                ('LName', models.CharField(max_length=200)),
                ('ownerType', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
