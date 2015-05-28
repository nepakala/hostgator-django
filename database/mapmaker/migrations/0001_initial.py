# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField(default=44.475833)),
                ('lon', models.FloatField(default=-73.211944)),
                ('imagelink', models.URLField(default=b'http://andyreagan.github.io')),
                ('location', models.CharField(default=b'Burlington, VT', max_length=200)),
                ('name', models.CharField(default=b'Andy Reagan', max_length=200)),
                ('description', models.TextField(default=b'Something about Andy')),
            ],
        ),
    ]
