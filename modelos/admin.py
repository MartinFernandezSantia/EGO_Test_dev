from django.contrib import admin
from modelos.models import Vehiculos, ModelosVehiculos, Imagenes, Colores


class InlineModelosVehiculos(admin.TabularInline):
    model = ModelosVehiculos
    extra = 0

class InlineImagenes(admin.TabularInline):
    model = Imagenes
    extra = 1

class AdminVehiculos(admin.ModelAdmin):
    inlines = [InlineModelosVehiculos, InlineImagenes]

    list_display = ["id_vehiculos","vehiculo", "price_formatted", "fecha", "tipo"]
    list_filter = ("tipo", "fecha")

    search_fields = ("vehiculo",)

class AdminModelosVehiculos(admin.ModelAdmin):
    list_display = ["modelo", "vehiculo"]

admin.site.register(Vehiculos, AdminVehiculos)
admin.site.register(ModelosVehiculos, AdminModelosVehiculos)
admin.site.register(Imagenes)
admin.site.register(Colores)

