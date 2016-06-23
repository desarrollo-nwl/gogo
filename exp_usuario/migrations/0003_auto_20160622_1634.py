# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exp_usuario', '0002_remove_colaboradoresexpusuario_colaborador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradoresexpusuario',
            name='id',
            field=models.OneToOneField(primary_key=True, serialize=False, to='colaboradores_360.Colaboradores_360'),
        ),
    ]
