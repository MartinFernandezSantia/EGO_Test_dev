from django.urls import path
from . import views

urlpatterns = [
    path("lista_vehiculos", views.lista_vehiculos, name="lista_vehiculos"),
    path("detalles_vehiculo/<int:id>", views.detalles_vehiculo, name="detalles_vehiculo"),
]
