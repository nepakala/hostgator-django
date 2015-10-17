# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapmaker', '0003_markup'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='company',
            field=models.TextField(default=b''),
        ),
    ]
