# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processor', '0004_auto_20151216_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processedcrash',
            name='crash_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crashsubmit.UploadedCrash', to_field='crash_id'),
        ),
    ]