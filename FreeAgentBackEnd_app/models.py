from django.db import models

# Create your models here.

class Equipo(models.Model):
    equipo_id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length= 30, blank= False)
    vacantes = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=False)
    numero_miembros = models.IntegerField()
    email = models.CharField(max_length=50, blank=False)
    equipos = models.Manager()

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    jugador_id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=False)
    alias = models.CharField(max_length=30, blank=False)
    password = models.CharField(max_length=30, blank=False)
    fecha_nacimiento = models.DateField(blank=False);
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length=50, blank=False);
    jugadores = models.Manager()

    def __str__(self):
        return self.alias

class Juego(models.Model):
    juego_id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False)
    genero = models.CharField(max_length=30, blank=False)
    pegI = models.CharField(max_length=10, blank=False)
    equipo = models.ManyToManyField(Equipo)
    juegos = models.Manager()

    def __str__(self):
        return self.nombre

class Cuota(models.Model):
    cuota_id = models.BigIntegerField(primary_key=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, blank=False)
    precio = models.DecimalField(max_digits=4, decimal_places=2, blank=False)
    renovacion_automatica = models.CharField(max_length=10, blank=False)
    fecha_inicio = models.DateField(blank=False)
    fecha_final = models.DateField(blank=False)
    cuotas = models.Manager()

    def __str__(self):
        return self.cuota_id

class Torneo(models.Model):
    torneo_id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False)
    fecha = models.DateField(blank=False)
    ciudad = models.CharField(max_length=20, blank=False)
    jugador = models.ManyToManyField(Jugador)
    torneos = models.Manager()

    def __str__(self):
        return self.nombre

class Oferta(models.Model):
    oferta_id = models.BigIntegerField(primary_key=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, blank=False)
    nombre = models.CharField(max_length=20, blank=False);
    descripcion = models.CharField(max_length=200, blank=False)
    numero_candidaturas = models.IntegerField(blank=False)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, blank=False)
    vacantes = models.IntegerField()
    jugador = models.ManyToManyField(Jugador)
    ofertas = models.Manager()

    def __str__(self):
        return self.nombre



