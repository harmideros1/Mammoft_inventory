from django.contrib import admin
from .models import FacturaClientes, FacturaProveedor, NotaCredito, NotaDebito

class FacturaClientesAdmin(admin.ModelAdmin):
    list_display = ["primer_numero","suiguiente_numero","ultimo_numero","prefijo","sufijo","comentario","id_periodo","cancelacion","bloqueo"]
    list_filter = ["primer_numero"]
    search_fields = ["primer_numero"]
    empty_value_display = '- Sin definir -'
    class Meta:
        model = FacturaClientes

class FacturaProveedorAdmin(admin.ModelAdmin):
    list_display = ["primer_numero","suiguiente_numero","ultimo_numero","prefijo","sufijo","comentario","id_periodo","cancelacion","bloqueo"]
    list_filter = ["primer_numero"]
    search_fields = ["primer_numero"]
    empty_value_display = '- Sin definir -'
    class Meta:
        model = FacturaProveedor

class NotaCreditoAdmin(admin.ModelAdmin):
    list_display = ["primer_numero","suiguiente_numero","ultimo_numero","prefijo","sufijo","comentario","id_periodo","cancelacion","bloqueo"]
    list_filter = ["primer_numero"]
    search_fields = ["primer_numero"]
    empty_value_display = '- Sin definir -'
    class Meta:
        model = NotaCredito

class NotaDebitoAdmin(admin.ModelAdmin):
    list_display = ["primer_numero","suiguiente_numero","ultimo_numero","prefijo","sufijo","comentario","id_periodo","cancelacion","bloqueo"]
    list_filter = ["primer_numero"]
    search_fields = ["primer_numero"]
    empty_value_display = '- Sin definir -'
    class Meta:
        model = NotaDebito

admin.site.register(FacturaClientes, FacturaClientesAdmin)
admin.site.register(FacturaProveedor, FacturaProveedorAdmin)
admin.site.register(NotaCredito, NotaCreditoAdmin)
admin.site.register(NotaDebito, NotaDebitoAdmin)
