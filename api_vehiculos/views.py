from django.shortcuts import render
from modelos.models import Vehiculos, ModelosVehiculos, Imagenes
# Create your views here.

def lista_vehiculos(request):
    vehiculos = []
    todos_vehiculos = Vehiculos.objects.all()

    for vehiculo in todos_vehiculos:
        params = {
            "id": vehiculo.id_vehiculos,
            "vehiculo": vehiculo.vehiculo,
            "precio": vehiculo.precio,
            "tipo": vehiculo.tipo,
            "fecha": vehiculo.fecha,
        }
        vehiculos.append(params)

    print(lista_vehiculos)

    return render(request, "api_vehiculos/lista_vehiculos.html", {"vehiculos": vehiculos})
    
def detalles_vehiculo(request, id):
    vehiculo = Vehiculos.objects.get(id_vehiculos=id)
    modelos = ModelosVehiculos.objects.filter(vehiculo=vehiculo)
    imagenes = Imagenes.objects.filter(vehiculo=vehiculo)

    params = {
        "vehiculo": {
            "id": vehiculo.id_vehiculos,
            "vehiculo": vehiculo.vehiculo,
            "precio": vehiculo.precio,
            "tipo": vehiculo.tipo,
            "fecha": vehiculo.fecha,
        },
    }

    lista_modelos = []

    for modelo in modelos:
        colores_modelo = modelo.colores.all()

        lista_modelos.append({
            "id": modelo.id_modelos_vehiculos,
            "modelo": modelo.modelo,
            "colores": [color.color for color in colores_modelo]
        }) 

    # lista_imagenes = []



    params["modelos"] = lista_modelos
    params["imagenes"] = [imagen.imagen for imagen in imagenes]

    print(params)

    return render(request, "api_vehiculos/detalles_vehiculo.html", params)