# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-25 12:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20180325_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseorg',
            old_name='course_nums',
            new_name='courses',
        ),
    ]
