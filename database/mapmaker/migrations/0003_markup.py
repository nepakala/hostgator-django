# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mapmaker', '0002_auto_20150528_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Markup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('before', models.TextField()),
                ('inbetween', models.TextField()),
                ('after', models.TextField()),
                ('jscode', models.TextField()),
                ('client', models.ForeignKey(related_name='markupcode', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
