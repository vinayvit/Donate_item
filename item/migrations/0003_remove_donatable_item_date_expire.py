# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_donatable_item_date_expire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donatable_item',
            name='Date_Expire',
        ),
    ]
