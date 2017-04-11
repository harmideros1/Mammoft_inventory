from django.db import models

class ParametrizacionDocumentos(models.Model):
    lst_ing_bruto = (('dato1','dato1'),('dato2','dato2'))
    lst_gan_ruta = (('dato1','dato1'),('dato2','dato2'))
    lst_stock = (('dato1','dato1'),('dato2','dato2'))
    calculo_ingreso_bruto = models.CharField(max_length=300, choices=lst_ing_bruto, default="",  verbose_name="Cálculo ingreso bruto")
    calculo_ganancia_ruta = models.CharField(max_length=300, choices=lst_gan_ruta, default="", verbose_name="Cálculo ganancia ruta")
    bloqueo_stock_negativos = models.CharField(max_length=300, choices=lst_stock, default="", verbose_name="Bloqueo stock negativos")

    class Meta:
        verbose_name_plural = "Configuraciones"
