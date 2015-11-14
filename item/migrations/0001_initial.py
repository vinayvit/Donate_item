# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donatable_item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=60)),
                ('Quality', models.IntegerField()),
                ('Zip_Code', models.CharField(max_length=6)),
                ('Address', models.CharField(max_length=60)),
                ('Description', models.TextField()),
                ('Date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('Date_Update', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
