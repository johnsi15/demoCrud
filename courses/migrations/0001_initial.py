# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('picture', models.ImageField(upload_to=b'media/course/pictures')),
            ],
        ),
    ]
