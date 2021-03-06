# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-03 23:55
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0057_job_per_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='simplified_geom',
            field=django.contrib.gis.db.models.fields.GeometryField(null=True,blank=True, srid=4326, verbose_name='Simplified geometry'),
        ),
        migrations.AlterField(
            model_name='job',
            name='the_geom',
            field=django.contrib.gis.db.models.fields.GeometryField(srid=4326, validators=[], verbose_name='Uploaded geometry'),
        ),
        migrations.RunSQL(
            "UPDATE jobs SET simplified_geom=ST_SimplifyPreserveTopology(the_geom, 0.01)"
        )
    ]
