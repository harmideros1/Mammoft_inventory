from django.db import models

class Sociedad(models.Model):
    nombre= models.CharField(max_length=300, default="")
    direccion = models.CharField(max_length=300, default="")
    apartado = models.CharField(max_length=300, default="")
    calle = models.CharField(max_length=300, default="")
    ciudad = models.CharField(max_length=300, default="")
    condado = models.CharField(max_length=300, default="")
    codigo_postal = models.CharField(max_length=10, default="")
    estado = models.CharField(max_length=300, default="")
    pais = models.CharField(max_length=300, default="")
    web = models.CharField(max_length=500, default="")
    telefono_uno = models.CharField(max_length=20, default="")
    telefono_dos = models.CharField(max_length=20, default="")
    correo = models.EmailField(help_text='Ingresa un correo válido por favor.', default="")

    class Meta:
        verbose_name_plural = "Sociedad"

class GestionContable(models.Model):
    ide_fiscal_nit = models.CharField(max_length=100, default="", verbose_name="Identificación Fiscal / Nit")
    hacienda = models.CharField(max_length=100, default="", verbose_name="Hacienda")
    ciu_consignacion = models.CharField(max_length=100, default="", verbose_name="Ciudad de consignación")
    calculo_amortizado = models.CharField(max_length=100, default="", verbose_name="Cálculo de amortización")
    activos_fijos = models.BooleanField(verbose_name="Permitir activos fijos")

    class Meta:
        verbose_name_plural = "Gestión Contable"
