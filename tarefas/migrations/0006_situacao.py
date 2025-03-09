# Generated by Django 5.1.4 on 2024-12-17 20:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0005_alter_tarefadia_tempo_gasto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.PositiveSmallIntegerField(choices=[(1, 'Iniciando'), (2, 'Explorando Ideias'), (3, 'Concentrado'), (4, 'Produtivo'), (5, 'Focado'), (6, 'Ritmo Constante'), (7, 'Pico de produtividade'), (8, 'Criativo')], default=1, verbose_name='Nível de concentração')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='situacao', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
