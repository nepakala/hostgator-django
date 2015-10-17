# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapmaker', '0004_city_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='company',
            field=models.TextField(default=b'', null=True),
        ),
    ]
