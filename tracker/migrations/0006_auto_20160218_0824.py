# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 08:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20160218_0823'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='connection',
            index_together=set([]),
        ),
    ]