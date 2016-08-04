# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '__first__'),
        ('colaboradores_360', '__first__'),
        ('cuestionarios_360', '__first__'),
        ('colaboradores', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriasProductos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(max_length=100)),
                ('observaciones', models.CharField(max_length=500)),
                ('proyecto', models.ForeignKey(blank=True, to='usuarios.Proyectos', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ColaboradoresExpUsuario',
            fields=[
                ('id', models.OneToOneField(primary_key=True, serialize=False, to='colaboradores.Colaboradores')),
                ('puntosLogrados', models.FloatField(default=0)),
                ('puntosDisponibles', models.FloatField(default=0)),
                ('colaborador', models.ForeignKey(blank=True, to='colaboradores_360.Colaboradores_360', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comentario', models.FloatField(max_length=500)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('colaboradorExpUsuario', models.ForeignKey(blank=True, to='exp_usuario.ColaboradoresExpUsuario', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lideres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lider', models.ForeignKey(blank=True, to='colaboradores_360.Colaboradores_360', null=True)),
                ('proyecto', models.ForeignKey(blank=True, to='usuarios.Proyectos', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan', models.CharField(max_length=500)),
                ('avance', models.FloatField(default=0)),
                ('impacto', models.FloatField(default=0)),
                ('fechaInicio', models.DateField(null=True, blank=True)),
                ('fechaFin', models.DateField(null=True, blank=True)),
                ('observaciones', models.CharField(max_length=500)),
                ('aprobacion', models.BooleanField(default=False)),
                ('estado', models.CharField(default=b'Sin Iniciar', max_length=200, null=True, blank=True)),
                ('lider', models.ForeignKey(blank=True, to='exp_usuario.Lideres', null=True)),
                ('proyecto', models.ForeignKey(blank=True, to='usuarios.Proyectos', null=True)),
                ('variables', models.ForeignKey(blank=True, to='cuestionarios_360.Variables_360', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producto', models.CharField(max_length=100)),
                ('puntos', models.FloatField(default=0)),
                ('observaciones', models.CharField(max_length=500, null=True, blank=True)),
                ('canjeado', models.FloatField(default=0)),
                ('categoria', models.ForeignKey(blank=True, to='exp_usuario.CategoriasProductos', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comentarios',
            name='plan',
            field=models.ForeignKey(blank=True, to='exp_usuario.Planes', null=True),
        ),
        migrations.AddField(
            model_name='colaboradoresexpusuario',
            name='lider',
            field=models.ForeignKey(blank=True, to='exp_usuario.Lideres', null=True),
        ),
        migrations.AddField(
            model_name='colaboradoresexpusuario',
            name='premiosCanjeados',
            field=models.ManyToManyField(to='exp_usuario.Productos', blank=True),
        ),
    ]
