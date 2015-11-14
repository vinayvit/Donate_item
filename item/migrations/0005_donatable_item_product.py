# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0004_auto_20151109_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='donatable_item',
            name='product',
            field=models.ForeignKey(default=datetime.datetime(2015, 11, 9, 9, 10, 6, 963395, tzinfo=utc), to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
