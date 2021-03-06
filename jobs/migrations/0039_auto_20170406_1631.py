# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-06 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0038_auto_20170406_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hdxexportregion',
            name='export_formats',
        ),
        migrations.RemoveField(
            model_name='hdxexportregion',
            name='feature_selection',
        ),
        migrations.RemoveField(
            model_name='hdxexportregion',
            name='last_run',
        ),
        migrations.RemoveField(
            model_name='hdxexportregion',
            name='name',
        ),
        migrations.RemoveField(
            model_name='hdxexportregion',
            name='the_geom',
        ),
        migrations.AddField(
            model_name='hdxexportregion',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.Job'),
        ),
        migrations.AddField(
            model_name='job',
            name='feature_selection',
            field=models.TextField(blank=True),
        ),
    ]
