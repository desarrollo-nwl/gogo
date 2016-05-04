# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exp_usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradoresexpusuario',
            name='premiosCanjeados',
            field=models.ManyToManyField(to='exp_usuario.Productos', blank=True),
        ),
    ]
