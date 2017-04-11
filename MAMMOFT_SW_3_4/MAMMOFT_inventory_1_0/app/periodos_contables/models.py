from django.db import models

class PeriodosContables(models.Model):
    lst_subperiodos = (('periodo1', 'periodo1'),('periodo2', 'periodo2'))

    codigo_periodo = models.CharField(max_length=300, default="", verbose_name="Código de periodo", primary_key=True)
    nombre_periodo = models.CharField(max_length=300, default="", verbose_name="Nombre")
    subperiodos = models.CharField(max_length=60,choices=lst_subperiodos, default="")
    fecha_contabilizacion = models.DateTimeField(auto_now=False)
    fecha_vencimiento = models.DateTimeField(auto_now=False)
    fecha_documento = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.nombre_periodo
    class Meta:
        verbose_name_plural = "Periodos"
