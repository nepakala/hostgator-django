# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mapmaker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='client',
            field=models.ForeignKey(related_name='cities', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='imagelink',
            field=models.URLField(default=b'http://newbreedmarketing.com'),
        ),
    ]
