# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_donatable_item_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donatable_item',
            name='product',
        ),
    ]
