# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuestionarios', '0001_initial'),
        ('colaboradores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Streaming',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fec_controlenvio', models.DateTimeField(null=True, blank=True)),
                ('fecharespuesta', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('colaborador', models.ForeignKey(to='colaboradores.Colaboradores')),
                ('pregunta', models.ForeignKey(to='cuestionarios.Preguntas')),
            ],
            options={
                'db_table': 'mensajeria_streaming',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StreamingRespuestas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('respuesta', models.CharField(max_length=350, null=True, blank=True)),
                ('streaming', models.ForeignKey(to='mensajeria.Streaming')),
            ],
            options={
                'db_table': 'mensajeria_streamingrespuestas',
                'managed': True,
            },
        ),
    ]
