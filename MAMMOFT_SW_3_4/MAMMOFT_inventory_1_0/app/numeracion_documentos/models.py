from django.db import models
from app.periodos_contables.models import PeriodosContables

class FacturaClientes(models.Model):
    primer_numero = models.IntegerField(default="0", verbose_name="Primer Número")
    suiguiente_numero = models.IntegerField(default="1", verbose_name="Siguiente Número")
    ultimo_numero = models.IntegerField(default="99999", verbose_name="Último Número")
    prefijo = models.CharField(max_length=300, default="", verbose_name="Prefijo")
    sufijo = models.CharField(max_length=300, default="", verbose_name="Sufijo")
    comentario = models.CharField(max_length=300, default="", verbose_name="Comentario")
    id_periodo = models.ForeignKey(PeriodosContables, default="001", verbose_name="Periodo")
    cancelacion = models.BooleanField(default=False, verbose_name="Cancelación")
    bloqueo = models.BooleanField(default=False, verbose_name="Bloqueo")

    class Meta:
        verbose_name_plural = "Facura Clientes"

class FacturaProveedor(models.Model):
    primer_numero = models.IntegerField(default="0", verbose_name="Primer Número")
    suiguiente_numero = models.IntegerField(default="1", verbose_name="Siguiente Número")
    ultimo_numero = models.IntegerField(default="99999", verbose_name="Último Número")
    prefijo = models.CharField(max_length=300, default="", verbose_name="Prefijo")
    sufijo = models.CharField(max_length=300, default="", verbose_name="Sufijo")
    comentario = models.CharField(max_length=300, default="", verbose_name="Comentario")
    id_periodo = models.ForeignKey(PeriodosContables, default="001", verbose_name="Periodo")
    cancelacion = models.BooleanField(default=False, verbose_name="Cancelación")
    bloqueo = models.BooleanField(default=False, verbose_name="Bloqueo")

    class Meta:
        verbose_name_plural = "Facura Proveedor"

class NotaCredito(models.Model):
    primer_numero = models.IntegerField(default="0", verbose_name="Primer Número")
    suiguiente_numero = models.IntegerField(default="1", verbose_name="Siguiente Número")
    ultimo_numero = models.IntegerField(default="99999", verbose_name="Último Número")
    prefijo = models.CharField(max_length=300, default="", verbose_name="Prefijo")
    sufijo = models.CharField(max_length=300, default="", verbose_name="Sufijo")
    comentario = models.CharField(max_length=300, default="", verbose_name="Comentario")
    id_periodo = models.ForeignKey(PeriodosContables, default="001", verbose_name="Periodo")
    cancelacion = models.BooleanField(default=False, verbose_name="Cancelación")
    bloqueo = models.BooleanField(default=False, verbose_name="Bloqueo")

    class Meta:
        verbose_name_plural = "Nota Crédito"

class NotaDebito(models.Model):
    primer_numero = models.IntegerField(default="0", verbose_name="Primer Número")
    suiguiente_numero = models.IntegerField(default="1", verbose_name="Siguiente Número")
    ultimo_numero = models.IntegerField(default="99999", verbose_name="Último Número")
    prefijo = models.CharField(max_length=300, default="", verbose_name="Prefijo")
    sufijo = models.CharField(max_length=300, default="", verbose_name="Sufijo")
    comentario = models.CharField(max_length=300, default="", verbose_name="Comentario")
    id_periodo = models.ForeignKey(PeriodosContables, default="001", verbose_name="Periodo")
    cancelacion = models.BooleanField(default=False, verbose_name="Cancelación")
    bloqueo = models.BooleanField(default=False, verbose_name="Bloqueo")

    class Meta:
        verbose_name_plural = "Nota Débito"
