# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaboradores',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('apellido', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=45)),
                ('key', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'colaboradores_colaboradores',
                'managed': True,
                'verbose_name_plural': 'Colaboradores',
            },
        ),
        migrations.CreateModel(
            name='ColaboradoresMetricas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fec_envio', models.DateTimeField(auto_now_add=True)),
                ('fec_respuesta', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'colaboradores_metricas',
                'managed': True,
                'verbose_name_plural': 'Metricas envio-repuesta',
            },
        ),
        migrations.CreateModel(
            name='RespuestasSalud',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fec_respuesta', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'colaboradores_respuestassalud',
                'managed': True,
                'verbose_name_plural': 'Respuestas salud colaboradores',
            },
        ),
        migrations.CreateModel(
            name='ColaboradoresDatos',
            fields=[
                ('id', models.OneToOneField(primary_key=True, serialize=False, to='colaboradores.Colaboradores')),
                ('area', models.CharField(max_length=50, null=True, blank=True)),
                ('car_ocupados', models.CharField(max_length=1000, null=True, blank=True)),
                ('cargo', models.CharField(max_length=200, null=True, blank=True)),
                ('dni', models.IntegerField(null=True, blank=True)),
                ('est_civil', models.CharField(max_length=15, null=True, blank=True)),
                ('fec_ingreso', models.DateField(null=True, blank=True)),
                ('fec_nacimiento', models.DateField(null=True, blank=True)),
                ('fec_retiro', models.IntegerField(null=True, blank=True)),
                ('genero', models.CharField(max_length=10, null=True, blank=True)),
                ('gente_a_cargo', models.BooleanField(default=True)),
                ('niv_academico', models.CharField(max_length=50, null=True, blank=True)),
                ('profesion', models.CharField(max_length=200, null=True, blank=True)),
                ('regional', models.CharField(max_length=50, null=True, blank=True)),
                ('sueldo', models.FloatField(null=True, blank=True)),
                ('vice', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'colaboradores_datos',
                'managed': True,
                'verbose_name_plural': 'Colaboradores datos',
            },
        ),
        migrations.CreateModel(
            name='ColaboradoresSalud',
            fields=[
                ('id', models.OneToOneField(primary_key=True, serialize=False, to='colaboradores.Colaboradores')),
                ('peso', models.FloatField(default=-1)),
            ],
            options={
                'db_table': 'colaboradores_salud',
                'managed': True,
                'verbose_name_plural': 'Colaboradores salud',
            },
        ),
        migrations.AddField(
            model_name='respuestassalud',
            name='colaborador',
            field=models.ForeignKey(to='colaboradores.Colaboradores'),
        ),
        migrations.AddField(
            model_name='colaboradoresmetricas',
            name='colaborador',
            field=models.ForeignKey(to='colaboradores.Colaboradores'),
        ),
    ]
