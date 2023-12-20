from django.contrib import admin
from modelos.models import Vehiculos, ModelosVehiculos, Imagenes, Colores


class InlineModelosVehiculos(admin.TabularInline):
    model = ModelosVehiculos
    extra = 0

class InlineImagenes(admin.TabularInline):
    model = Imagenes
    extra = 1

# Seccion para los vehiculos en el panel admin
class AdminVehiculos(admin.ModelAdmin):
    inlines = [InlineModelosVehiculos, InlineImagenes]

    list_display = ["id","vehiculo", "price_formatted", "fecha", "tipo"]
    list_filter = ("tipo", "fecha")

    search_fields = ("vehiculo",)

# Seccion para los modelos de los vehiculos en el panel admin
class AdminModelosVehiculos(admin.ModelAdmin):
    list_display = ["modelo", "vehiculo"]

admin.site.register(Vehiculos, AdminVehiculos)
admin.site.register(ModelosVehiculos, AdminModelosVehiculos)
admin.site.register(Imagenes)
admin.site.register(Colores)

