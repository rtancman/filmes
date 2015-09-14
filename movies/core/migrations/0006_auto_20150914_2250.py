# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150914_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.ManyToManyField(to=b'core.Category', null=True, blank=True),
        ),
    ]
