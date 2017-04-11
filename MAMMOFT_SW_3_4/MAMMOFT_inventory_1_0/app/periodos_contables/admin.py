from django.contrib import admin
from .models import PeriodosContables

class PeriodosContablesAdmin(admin.ModelAdmin):
    list_display = ["codigo_periodo","nombre_periodo","subperiodos","fecha_contabilizacion","fecha_vencimiento","fecha_documento"]
    list_filter = ["codigo_periodo"]
    search_fields = ["codigo_periodo"]
    empty_value_display = '- Sin definir -'
    class Meta:
        model = PeriodosContables

admin.site.register(PeriodosContables, PeriodosContablesAdmin)
