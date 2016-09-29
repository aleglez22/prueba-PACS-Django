# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.BigIntegerField()),
                ('time', models.DateTimeField()),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100, default='calle')),
            ],
        ),
    ]
