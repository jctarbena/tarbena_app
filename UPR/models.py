from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

import os
import datetime

# Create your models here.
class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating
    ``created`` and ``modified`` fields.
    """

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


    class Meta:
        abstract = True

def upload_location(instance, filename):
    return os.path.join('UPR/img/', datetime.datetime.now().date().strftime("%Y/%m/%d"), filename)

class TipoMaquina(TimeStampedModel):
    tipo = models.CharField(max_length=250, blank=True, null=True)
    img_maquina = models.ImageField(upload_to=upload_location, null=True, blank=True)
    url_tienda_maquina = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.tipo)

class GrupoComponentes(TimeStampedModel):
    tipo_grupo_componentes = models.CharField(max_length=250, blank=True, null=True)
    position_grupo_componentes = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.tipo_grupo_componentes)

class Provincia(TimeStampedModel):
    nombre = models.CharField(max_length=250, blank=True, null=True)
    codigo = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Provincia'
        verbose_name_plural = "Provincias"

    def __str__(self):
        return '{}, {}'.format(self.nombre, self.nombre)

class Comarca(TimeStampedModel):
    nombre = models.CharField(max_length=250, blank=True, null=True)
    capital = models.CharField(max_length=250, blank=True, null=True)
    habitantes = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    provincia = models.ForeignKey(Provincia, blank=True, null=True)
    km_cuadrados = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return '{}, {}'.format(self.nombre, self.nombre)

class Poblacion(TimeStampedModel):
    nombre = models.CharField(max_length=250, blank=True, null=True)
    codigo_INE = models.CharField(max_length=250, blank=True, null=True)
    comarca = models.ForeignKey(Comarca, blank=True, null=True)
    orden_noel = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["codigo_INE"]
        verbose_name = 'Poblacion'
        verbose_name_plural = "Poblaciones"

    def __str__(self):
        return '{}, {}'.format(self.codigo_INE, self.nombre)

class Componentes(TimeStampedModel):
    tipo_componentes = models.CharField(max_length=250, blank=True, null=True)
    tipo_comentario = models.TextField(blank=True, null=True)
    imatge_componente = models.ImageField(upload_to=upload_location, null=True, blank=True)
    tipo_maquina = models.ManyToManyField(TipoMaquina, blank=True, related_name='tipo_maquina_componente')
    grupo_componentes = models.ForeignKey(GrupoComponentes, blank=True, null=True, related_name='grupo_componentes')

    def __str__(self):
        return '{}'.format(self.tipo_componentes)

    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'


class Incidencias(TimeStampedModel):
    tipo_incidencias = models.ForeignKey(Componentes, blank=True, null=True, related_name='tipo_componente')
    fecha = models.DateField(blank=True, null=True)
    cerrado = models.BooleanField(default=True)
    comentario = models.TextField(blank=True, null=True)
    revision_fin_temporada_2019 = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.tipo_incidencias)

    class Meta:
        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'

class Maquina(TimeStampedModel):
    numero_inventario = models.CharField(max_length=250, blank=True, null=True)
    numero_serie = models.CharField(max_length=250, blank=True, null=True)
    fecha_compra = models.DateField(blank=True, null=True)
    tipo_maquina = models.ForeignKey(TipoMaquina, blank=True, null=True, related_name='tipo_maquinas')
    incidencias = models.ManyToManyField(Incidencias, blank=True, related_name='tipo_incidencia')
    #incidencias = models.ManyToManyField(Incidencias, blank=True, null=True, limit_choices_to={'fechas' != ''})
    capataz_responsable = models.ForeignKey(User, blank=True, null=True, limit_choices_to={'groups__name': "UPR"})
    poblacion = models.ForeignKey(Poblacion, blank=True, null=True, related_name='nombrePoblacionMaquina')
    #maquina_poblacion = models.ForeignKey(Poblacion, blank=True, null=True, related_name='nombre_poblacion')
    def __str__(self):
        return '{}'.format(self.numero_inventario)

class MovimientoMaquinaria(TimeStampedModel):
    fecha_movimiento = models.DateField(blank=True, null=True)
    numero_inventario_mm = models.ForeignKey(Maquina, blank=True, null=True, related_name='numeroInventario')
    poblacion_mm = models.ForeignKey(Poblacion, blank=True, null=True, related_name='nombrePoblacion')

    def __str__(self):
        return '{}'.format(self.numero_inventario_mm)

    class Meta:
        ordering = ['-fecha_movimiento',]

class RevisionesTemporada(TimeStampedModel):
    nombre_revision = models.CharField(max_length=250, blank=True, null=True)
    fecha_revisión = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre_revision)