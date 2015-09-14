# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='author',
            field=models.ManyToManyField(to=b'core.Author', null=True, blank=True),
        ),
    ]
