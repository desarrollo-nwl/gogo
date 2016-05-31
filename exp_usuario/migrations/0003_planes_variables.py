# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuestionarios_360', '__first__'),
        ('exp_usuario', '0002_planes_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='planes',
            name='variables',
            field=models.ForeignKey(blank=True, to='cuestionarios_360.Variables_360', null=True),
        ),
    ]
