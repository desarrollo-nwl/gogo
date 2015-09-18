# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('cuestionarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='variables',
            name='proyecto',
            field=models.ForeignKey(blank=True, to='usuarios.Proyectos', null=True),
        ),
        migrations.AddField(
            model_name='respuestas',
            name='pregunta',
            field=models.ForeignKey(to='cuestionarios.Preguntas'),
        ),
        migrations.AddField(
            model_name='preguntas',
            name='variable',
            field=models.ForeignKey(to='cuestionarios.Variables'),
        ),
        migrations.AddField(
            model_name='bibliotecas',
            name='variables',
            field=models.ManyToManyField(to='cuestionarios.Variables'),
        ),
    ]
