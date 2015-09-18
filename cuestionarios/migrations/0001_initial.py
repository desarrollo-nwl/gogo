# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bibliotecas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.TextField(max_length=255, null=True, blank=True)),
                ('nombre', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'db_table': 'cuestionario_bibliotecas',
                'managed': True,
                'verbose_name_plural': 'Bibliotecas',
            },
        ),
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('abierta', models.BooleanField(default=False)),
                ('estado', models.BooleanField(default=True)),
                ('multiple', models.BooleanField(default=False)),
                ('numerica', models.BooleanField(default=True)),
                ('posicion', models.IntegerField()),
                ('texto', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cuestionarios_preguntas',
                'managed': True,
                'verbose_name_plural': 'Preguntas',
            },
        ),
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('numerico', models.FloatField(null=True, blank=True)),
                ('texto', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cuestionarios_respuestas',
                'managed': True,
                'verbose_name_plural': 'Respuestas',
            },
        ),
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.TextField(max_length=255, null=True, blank=True)),
                ('estado', models.BooleanField(default=True)),
                ('max_preguntas', models.PositiveSmallIntegerField(default=0)),
                ('nombre', models.CharField(max_length=255)),
                ('posicion', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'cuestionarios_variables',
                'managed': True,
                'verbose_name_plural': 'Variables',
            },
        ),
    ]
