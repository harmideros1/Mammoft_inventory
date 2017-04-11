from django.contrib import admin
from .models import Sociedad, GestionContable

class SociedadAdmin(admin.ModelAdmin):
    list_display = ["nombre", "direccion", "apartado", "calle", "ciudad", "condado", "codigo_postal", "estado", "pais", "web", "telefono_uno", "telefono_dos", "correo"]
    list_filter = ["nombre"]
    search_fields = ["nombre"]
    empty_value_display = '- Sin definir -'
    class Meta:
        model = Sociedad

class GestionContableAdmin(admin.ModelAdmin):
    list_display = ["ide_fiscal_nit", "hacienda", "ciu_consignacion","calculo_amortizado","activos_fijos"]
    list_filter = ["ide_fiscal_nit"]
    search_fields = ["ide_fiscal_nit"]
    empty_value_display = '- Sin definir -'
    class Meta:
        model = GestionContable

admin.site.register(Sociedad, SociedadAdmin)
admin.site.register(GestionContable, GestionContableAdmin)
