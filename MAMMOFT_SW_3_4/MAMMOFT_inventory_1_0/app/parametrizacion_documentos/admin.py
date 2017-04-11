from django.contrib import admin
from .models import ParametrizacionDocumentos

class ParametrizacionDocumentosAdmin(admin.ModelAdmin):
    list_display = ["calculo_ingreso_bruto","calculo_ganancia_ruta","bloqueo_stock_negativos"]
    list_filter = ["calculo_ingreso_bruto"]
    search_fields = ["calculo_ingreso_bruto"]
    empty_value_display = '- Sin definir -'
    class Meta:
        model = ParametrizacionDocumentos

admin.site.register(ParametrizacionDocumentos, ParametrizacionDocumentosAdmin)
