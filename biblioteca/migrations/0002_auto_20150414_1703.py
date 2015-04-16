# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ['titulo']},
        ),
    ]
