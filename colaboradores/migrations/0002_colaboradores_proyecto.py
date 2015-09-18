# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('colaboradores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaboradores',
            name='proyecto',
            field=models.ForeignKey(to='usuarios.Proyectos'),
        ),
    ]
