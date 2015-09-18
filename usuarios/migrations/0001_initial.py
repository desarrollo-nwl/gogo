# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('activa', models.BooleanField(default=True)),
                ('departamento', models.CharField(max_length=100, null=True, blank=True)),
                ('nit', models.CharField(max_length=20, null=True, blank=True)),
                ('nombre', models.CharField(max_length=100)),
                ('num_empleados', models.IntegerField(null=True, blank=True)),
                ('pagina', models.CharField(max_length=1000, null=True, blank=True)),
                ('pais', models.CharField(max_length=100, null=True, blank=True)),
                ('sector', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'usuarios_empresas',
                'managed': True,
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='IndiceUsuarios',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, db_index=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, to='usuarios.IndiceUsuarios', null=True)),
            ],
            options={
                'db_table': 'usuarios_indice',
                'managed': True,
                'verbose_name_plural': 'Indice de usuarios',
            },
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('consultor', models.BooleanField(default=True)),
                ('cre_usuarios', models.BooleanField(default=False)),
                ('act_surveys', models.BooleanField(default=False)),
                ('act_variables', models.BooleanField(default=True)),
                ('col_add', models.BooleanField(default=True)),
                ('col_del', models.BooleanField(default=True)),
                ('col_edit', models.BooleanField(default=True)),
                ('col_see', models.BooleanField(default=True)),
                ('det_see', models.BooleanField(default=True)),
                ('pre_add', models.BooleanField(default=True)),
                ('pre_del', models.BooleanField(default=True)),
                ('pre_edit', models.BooleanField(default=True)),
                ('pre_see', models.BooleanField(default=True)),
                ('pro_add', models.BooleanField(default=True)),
                ('pro_del', models.BooleanField(default=True)),
                ('pro_edit', models.BooleanField(default=True)),
                ('pro_see', models.BooleanField(default=True)),
                ('res_exp', models.BooleanField(default=True)),
                ('res_see', models.BooleanField(default=True)),
                ('var_add', models.BooleanField(default=True)),
                ('var_del', models.BooleanField(default=True)),
                ('var_edit', models.BooleanField(default=True)),
                ('var_see', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'usuarios_permisos',
                'managed': True,
                'verbose_name_plural': 'Permisos',
            },
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('activo', models.BooleanField(default=False)),
                ('can_envio', models.IntegerField(default=5)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('fec_registro', models.DateTimeField(auto_now_add=True)),
                ('iniciable', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=255)),
                ('prudenciamax', models.IntegerField(default=2)),
                ('prudenciamin', models.IntegerField(default=1)),
                ('max_variables', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'db_table': 'cuestionarios_proyectos',
                'managed': True,
                'verbose_name_plural': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='Recuperar',
            fields=[
                ('id_envio', models.AutoField(serialize=False, primary_key=True)),
                ('link', models.CharField(max_length=96)),
                ('fregistro', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'usuarios_recuperar',
                'managed': True,
                'verbose_name_plural': 'Recuperar',
            },
        ),
        migrations.CreateModel(
            name='ProyectosDatos',
            fields=[
                ('id', models.OneToOneField(primary_key=True, serialize=False, to='usuarios.Proyectos')),
                ('cue_correo', models.TextField(null=True, blank=True)),
                ('fregistro', models.DateField(auto_now_add=True)),
                ('int_encuesta', models.TextField(null=True, blank=True)),
                ('logo', models.ImageField(upload_to='logos')),
                ('logoenc', models.ImageField(null=True, upload_to='logos', blank=True)),
                ('senso', models.BooleanField(default=False)),
                ('tipo', models.IntegerField(null=True, blank=True)),
                ('tit_encuesta', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'cuestionarios_proyectosdatos',
                'managed': True,
                'verbose_name_plural': 'Proyectos datos',
            },
        ),
        migrations.AddField(
            model_name='proyectos',
            name='empresa',
            field=models.ForeignKey(to='usuarios.Empresas'),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='usuarios',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='indiceusuarios',
            name='usuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='empresas',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
