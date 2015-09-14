# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150914_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
