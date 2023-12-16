from django.db import models
from django.utils import timezone

# Create your models here.
class Colores(models.Model):
    id_colores = models.AutoField(primary_key=True)
    color = models.CharField(max_length=30, null=False, blank=False)

class Imagenes(models.Model):
    id_imagen_modelo = models.AutoField(primary_key=True)
    imagen = models.ImageField(null=False, blank=False, upload_to="imagenes_modelos/")

class Vehiculos(models.Model):
    AUTO = "Auto"
    PICKUP = "Pickup"
    COMERCIAL = "Comercial"
    SUV = "SUV"
    CROSSOVER = "CrossOver"

    OPCIONES = [
        (AUTO, "Auto"),
        (PICKUP, "Pickup"),
        (COMERCIAL, "Comercial"),
        (SUV, "SUV"),
        (CROSSOVER, "CrossOver"),
    ]

    id_vehiculos = models.AutoField(primary_key=True)
    vehiculo = models.CharField(max_length=100, blank=False, null=False, unique=True)
    precio = models.FloatField(null=True, blank=False)
    fecha = models.DateField(null=True, blank=False, default=timezone.now)
    tipo = models.CharField(max_length=10, choices=OPCIONES)
    imagenes = models.ManyToManyField(Imagenes)
    

class ModelosVehiculos(models.Model):
    id_modelos_vehiculos = models.AutoField(primary_key=True)
    id_vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100, null=False, blank=False)
    colores = models.ManyToManyField(Colores)
