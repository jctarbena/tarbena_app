from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Contador, Factura

# Register your models here.
class FacturaInline(admin.TabularInline):
    model = Factura
    extra = 0
    show_change_link = True

class ContadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'codigo',)
    list_filter = ['nombre']
    search_fields = ('nombre', 'descripcion', 'codigo',)
    empty_value_display = '-'
    list_display_links = ('nombre',)
    show_full_result_count = True

    inlines = [FacturaInline]
admin.site.register(Contador, ContadorAdmin)

class FacturaAdmin(ImportExportModelAdmin):
    list_display = ('desde', 'hasta', 'cantidad', 'lectura_anterior', 'lectura_posterior', 'consumo', 'contador')
    list_filter = ['contador__nombre', 'desde', 'hasta']
    search_fields = ('contador__nombre' ,'desde', 'hasta', 'cantidad', 'lectura_anterior', 'lectura_posterior', 'consumo',)
    empty_value_display = '-'
    list_display_links = ('desde',)
    show_full_result_count = True
    date_hierarchy = 'desde'
    list_select_related = (
        'contador',
    )
admin.site.register(Factura, FacturaAdmin)