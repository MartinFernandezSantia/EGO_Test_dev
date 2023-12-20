from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
from django.core.exceptions import ValidationError
from django.contrib import admin


# Colores de los vehiculos
class Colores(models.Model):
    class Meta:  
        verbose_name_plural = 'Colores'

    id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.color

# Tabla de los vehiculos
class Vehiculos(models.Model):
    class Meta:  
            verbose_name_plural = 'Vehiculos'

    def validar_cuatro_digitos(value):
        if not (1800 <= value <= 3000):
            raise ValidationError("El valor ingresado debe ser un año.")
        
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

    id = models.AutoField(primary_key=True)
    vehiculo = models.CharField(max_length=100, blank=False, null=False, unique=True)
    precio = models.FloatField(null=True, blank=False)
    fecha = models.IntegerField(validators=[validar_cuatro_digitos], null=True, blank=False)
    tipo = models.CharField(max_length=10, choices=OPCIONES)

    def __str__(self):
        return self.vehiculo

    # Formatear el precio con separadores de miles
    @property
    @admin.display(description='precio', ordering='precio')
    def price_formatted(self):
        return f"{self.precio:,}"

    

# Tabla modelos de los vehiculos, cada vehiculo puede tener mas de un modelo
class ModelosVehiculos(models.Model):
    class Meta:  
        verbose_name_plural = 'Modelos de Vehiculos'

    id = models.AutoField(primary_key=True)
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100, null=False, blank=False)
    colores = models.ManyToManyField(Colores)

    def __str__(self):
        return self.modelo

# Imagenes relacionadas al vehiculo
class Imagenes(models.Model):
    class Meta:  
        verbose_name_plural = 'Imagenes'

    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(null=False, blank=False, upload_to="imagenes_modelos/")
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)

    def __str__(self):
            return self.imagen.path

# Funcion que elimina la imagen en la carpeta "media/imagenes_modelos/" cuando se borra la instacia asociada
#   a la misma en la tabla Imagenes
@receiver(pre_delete, sender=Imagenes)
def borrar_imagen(sender, instance, **kwargs):
    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)