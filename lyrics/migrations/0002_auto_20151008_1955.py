# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='writers',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='verse',
            name='verse_text',
            field=models.TextField(),
        ),
    ]
