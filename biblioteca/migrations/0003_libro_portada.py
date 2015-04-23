# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_auto_20150414_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='portada',
            field=models.ImageField(default=datetime.datetime(2015, 4, 17, 22, 3, 45, 351737, tzinfo=utc), upload_to=b'portadas'),
            preserve_default=False,
        ),
    ]
