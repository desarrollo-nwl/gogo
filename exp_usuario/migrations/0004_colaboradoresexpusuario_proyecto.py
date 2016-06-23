# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '__first__'),
        ('exp_usuario', '0003_auto_20160622_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaboradoresexpusuario',
            name='proyecto',
            field=models.ForeignKey(blank=True, to='usuarios.Proyectos', null=True),
        ),
    ]
