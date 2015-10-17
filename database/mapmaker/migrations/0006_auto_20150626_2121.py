# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapmaker', '0005_auto_20150626_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='company',
            field=models.TextField(default=b'', null=True, blank=True),
        ),
    ]
