# Generated by Django 4.2 on 2023-12-16 00:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Colores",
            fields=[
                ("id_colores", models.AutoField(primary_key=True, serialize=False)),
                ("color", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Imagenes",
            fields=[
                (
                    "id_imagen_modelo",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("imagen", models.ImageField(upload_to="imagenes_modelos/")),
            ],
        ),
        migrations.CreateModel(
            name="Vehiculos",
            fields=[
                ("id_vehiculos", models.AutoField(primary_key=True, serialize=False)),
                ("vehiculo", models.CharField(max_length=100, unique=True)),
                ("precio", models.FloatField(null=True)),
                (
                    "fecha",
                    models.DateField(default=django.utils.timezone.now, null=True),
                ),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("Auto", "Auto"),
                            ("Pickup", "Pickup"),
                            ("Comercial", "Comercial"),
                            ("SUV", "SUV"),
                            ("CrossOver", "CrossOver"),
                        ],
                        max_length=10,
                    ),
                ),
                ("imagenes", models.ManyToManyField(to="modelos.imagenes")),
            ],
        ),
        migrations.CreateModel(
            name="ModelosVehiculos",
            fields=[
                (
                    "id_modelos_vehiculos",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("modelo", models.CharField(max_length=100)),
                ("colores", models.ManyToManyField(to="modelos.colores")),
                (
                    "id_vehiculo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modelos.vehiculos",
                    ),
                ),
            ],
        ),
    ]