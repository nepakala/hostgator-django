# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapmaker', '0006_auto_20150626_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='markup',
            name='version',
            field=models.IntegerField(default=1),
        ),
    ]
