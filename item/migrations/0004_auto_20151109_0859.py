# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_remove_donatable_item_date_expire'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donatable_item',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='donatable_item',
            old_name='Date_Update',
            new_name='date_Update',
        ),
        migrations.RenameField(
            model_name='donatable_item',
            old_name='Date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='donatable_item',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='donatable_item',
            old_name='Quality',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='donatable_item',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='donatable_item',
            old_name='Zip_Code',
            new_name='zip_Code',
        ),
        migrations.AddField(
            model_name='donatable_item',
            name='expire_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
