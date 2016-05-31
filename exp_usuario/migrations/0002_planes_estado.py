# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exp_usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planes',
            name='estado',
            field=models.CharField(default=b'Sin Iniciar', max_length=200, null=True, blank=True),
        ),
    ]
