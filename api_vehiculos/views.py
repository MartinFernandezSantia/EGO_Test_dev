from django.shortcuts import render
from modelos.models import Vehiculos, ModelosVehiculos, Imagenes, Colores
from django.http import JsonResponse, HttpResponseNotFound, Http404

# Funcion general para obtener todos los objetos o un objeto por id de cualquiera de los modelos
def obtener_objectos(request, objetos, tipo_objeto, id=None):
    if id is None:
        # Si no se proporciona un ID, devuelve todos los colores
        return JsonResponse({tipo_objeto: list(objetos())})
    else:
        # Si se proporciona un ID, intenta obtener ese color
        try:
            objeto = objetos().get(id=id)
            return JsonResponse({tipo_objeto: objeto})
        except:
            return HttpResponseNotFound("El objeto no existe")


# Funcion para procesar los parametros enviados por la URL y llamar a obtener_objetos()
def procesar_consulta(request, objeto, id=None):
    modelos = {
        "imagenes": Imagenes.objects.values,
        "colores": Colores.objects.values,
        "vehiculos": Vehiculos.objects.values,
        "modelos_vehiculos": ModelosVehiculos.objects.values,
    }
    # Si el objeto no coincide con uno de los modelos
    if objeto not in modelos.keys():
        raise Http404("Esta pagina no extiste")
    
    return obtener_objectos(request, modelos[objeto], objeto, id)
    
    
