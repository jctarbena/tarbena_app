from django.contrib import admin

# Register your models here.

from .models import Maquina, TipoMaquina, Componentes, Incidencias, GrupoComponentes, Poblacion, Comarca, Provincia, MovimientoMaquinaria, RevisionesTemporada, Obra, MantenimientoMaquinaria, MovimientoObra, OpcionesComponente, PuebloAsignado


## POBLACIONES, COMARCAS Y PROVINCIAS
##
class PoblacionAdmin(admin.ModelAdmin):
    list_display = ('nombre','codigo_INE',)
    list_filter = ('nombre','codigo_INE',)
    search_fields = ('nombre','codigo_INE')
    empty_value_display = '-'
    list_display_links = ('nombre',)
    show_full_result_count = True
admin.site.register(Poblacion, PoblacionAdmin)

class ComarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre','capital','habitantes','km_cuadrados','provincia',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)
    empty_value_display = '-'
    list_display_links = ('nombre',)
    show_full_result_count = True
admin.site.register(Comarca, ComarcaAdmin)

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)
    empty_value_display = '-'
    list_display_links = ('nombre',)
    show_full_result_count = True
admin.site.register(Provincia, ProvinciaAdmin)


class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('numero_inventario', 'numero_serie', 'fecha_compra','tipo_maquina','capataz_responsable',)
    list_filter = ['tipo_maquina__tipo', 'numero_inventario',]
    search_fields = ('numero_inventario', 'numero_serie', 'tipo_maquina',)
    empty_value_display = '-'
    list_display_links = ('numero_inventario',)
    show_full_result_count = True
admin.site.register(Maquina, MaquinaAdmin)


class TipoMaquinaAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
    list_filter = ['tipo']
    search_fields = ('tipo',)
    empty_value_display = '-'
    list_display_links = ('tipo',)
    show_full_result_count = True
admin.site.register(TipoMaquina, TipoMaquinaAdmin)

class GrupoComponentesAdmin(admin.ModelAdmin):
    list_display = ('tipo_grupo_componentes','position_grupo_componentes',)
    list_filter = ['tipo_grupo_componentes']
    search_fields = ('tipo_grupo_componentes',)
    empty_value_display = '-'
    list_display_links = ('tipo_grupo_componentes',)
    show_full_result_count = True
admin.site.register(GrupoComponentes, GrupoComponentesAdmin)

class ComponentesAdmin(admin.ModelAdmin):
    list_display = ('tipo_componentes','tipo_comentario','imatge_componente','tipo_maquina_display','grupo_componentes','opciones_componente_display',)
    list_filter = ['tipo_componentes']
    search_fields = ('tipo_componentes',)
    empty_value_display = '-'
    list_display_links = ('tipo_componentes',)
    show_full_result_count = True

    def tipo_maquina_display(self, obj):
        return ", ".join([
            maquina.tipo for maquina in obj.tipo_maquina.all()
        ])
    tipo_maquina_display.short_description = "Tipo maquina"

    def opciones_componente_display(self, obj):
        return ", ".join([
            incidencias.nombre for incidencias in obj.opciones_componente.all()
        ])
    opciones_componente_display.short_description = "Opciones componente"

#    def position_grupo_componentes_display(self, obj):
#        return ", ".join([
#            grupoComponentes.
#        ])
admin.site.register(Componentes, ComponentesAdmin)

class IncidenciasAdmin(admin.ModelAdmin):
    list_display = ('tipo_incidencias','n_inventario','fecha','fechaCerrado','comentario',)
    list_filter = ('tipo_incidencias__tipo_componentes',)
    search_fields = ('tipo_incidencias',)
    empty_value_display = '-'
    list_display_links = ('tipo_incidencias',)
    show_full_result_count = True
admin.site.register(Incidencias, IncidenciasAdmin)

class MovimientoMaquinariaAdmin(admin.ModelAdmin):
    list_display = ('poblacion_mm','fecha_movimiento',)
    list_filter = ('poblacion_mm','fecha_movimiento',)
    search_fields = ('poblacion_mm',)
    empty_value_display = '-'
    list_display_links = ('poblacion_mm',)
    show_full_result_count = True
admin.site.register(MovimientoMaquinaria, MovimientoMaquinariaAdmin)

class PuebloAsignadoAdmin(admin.ModelAdmin):
    list_display = ('nombre','fecha_movimiento',)
    list_filter = ('nombre','fecha_movimiento',)
    search_fields = ('nombre',)
    empty_value_display = '-'
    list_display_links = ('nombre',)
    show_full_result_count = True
admin.site.register(PuebloAsignado, PuebloAsignadoAdmin)

class RevisionesTemporadaAdmin(admin.ModelAdmin):
    list_display = ('nombre_revision','fecha_revision',)
    list_filter = ('nombre_revision', 'fecha_revision',)
    search_fields = ('nombre_revision',)
    empty_value_display = '-'
    list_display_links = ('nombre_revision',)
    show_full_result_count = True
admin.site.register(RevisionesTemporada, RevisionesTemporadaAdmin)

class MantenimientoMaquinariaAdmin(admin.ModelAdmin):
    list_display = ('nombre_revision','numero_maquina','numero_incidencia',)
    list_filter = ('nombre_revision','numero_maquina','numero_incidencia',)
    search_fields = ('nombre_revision',)
    empty_value_display = '-'
    list_display_links = ('nombre_revision',)
    show_full_result_count = True
admin.site.register(MantenimientoMaquinaria, MantenimientoMaquinariaAdmin)

class ObraAdmin(admin.ModelAdmin):
    list_display = ('nombre_obra',)
    list_filter = ('nombre_obra',)
    search_fields = ('nombre_obra',)
    empty_value_display = '-'
    list_display_links = ('nombre_obra',)
    show_full_result_count = True
admin.site.register(Obra, ObraAdmin)

class MovimientoObraAdmin(admin.ModelAdmin):
    list_display = ('fecha_movimiento','nombre_obra','comentario')
    list_filter = ('nombre_obra',)
    search_fields = ('nombre_obra',)
    empty_value_display = '-'
    list_display_links = ('nombre_obra',)
    show_full_result_count = True
admin.site.register(MovimientoObra, MovimientoObraAdmin)

class OpcionesComponenteAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_display_links = ('nombre',)
admin.site.register(OpcionesComponente, OpcionesComponenteAdmin)