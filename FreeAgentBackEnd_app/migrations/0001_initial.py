# Generated by Django 3.0.3 on 2020-03-10 13:48

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('equipo_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('vacantes', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('numero_miembros', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
            managers=[
                ('equipos', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('juego_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
                ('pegI', models.CharField(max_length=10)),
                ('equipo', models.ManyToManyField(to='FreeAgentBackEnd_app.Equipo')),
            ],
            managers=[
                ('juegos', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('jugador_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('alias', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.CharField(max_length=50)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreeAgentBackEnd_app.Equipo')),
            ],
            managers=[
                ('jugadores', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('torneo_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('ciudad', models.CharField(max_length=20)),
                ('jugador', models.ManyToManyField(to='FreeAgentBackEnd_app.Jugador')),
            ],
            managers=[
                ('torneos', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('oferta_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=200)),
                ('numero_candidaturas', models.IntegerField()),
                ('vacantes', models.IntegerField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreeAgentBackEnd_app.Equipo')),
                ('juego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreeAgentBackEnd_app.Juego')),
                ('jugador', models.ManyToManyField(to='FreeAgentBackEnd_app.Jugador')),
            ],
            managers=[
                ('ofertas', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Cuota',
            fields=[
                ('cuota_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=4)),
                ('renovacion_automatica', models.CharField(max_length=10)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreeAgentBackEnd_app.Equipo')),
            ],
            managers=[
                ('cuotas', django.db.models.manager.Manager()),
            ],
        ),
    ]
