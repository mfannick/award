# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-31 07:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awardapp', '0003_auto_20191031_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='projectF',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='awardapp.Project'),
        ),
    ]