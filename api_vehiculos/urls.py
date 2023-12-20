from django.urls import path
from . import views

urlpatterns = [
    path('api/<str:objeto>/', views.procesar_consulta, name='obtener_objetos'),    
    path('api/<str:objeto>/<int:id>/', views.procesar_consulta, name='obtener_imagenes_por_id')
]
