from django.contrib import messages
from django.core import serializers
from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView

from .models import Maquina, TipoMaquina, Componentes, Incidencias, MovimientoMaquinaria, Poblacion, GrupoComponentes, RevisionesTemporada, Obra, MantenimientoMaquinaria, MovimientoObra
from .forms import MaquinaIncidenciasForm, MovimientoMaquinariaForm, MovimientoObraForm

# Create your views here.
# --------------- Maquina Index --------------- #
@login_required()
def index_maquinas(request):
    maquinas = Maquina.objects.all()
    # movimientos = Maquina.maquina_poblacion.poblacion_mm.order_by('-fecha_movimiento')[0]
    llegandoCerrado = Maquina.objects.select_related(
        'tipo_maquina', 'capataz_responsable',
    ).prefetch_related('incidencias')
    return render(request,
                  'UPR/index.html',
                  {'maquinas':maquinas,
                   'llegandoCerrado':llegandoCerrado})

# --------------- Maquina Details --------------- #
# /upr/maquina/721721/

def maquina_detail(request, ninventario):
    maquina = get_object_or_404(Maquina.objects.select_related(
                                            'tipo_maquina','capataz_responsable',
    ).prefetch_related('incidencias').order_by('indicencias__fecha'),
                                numero_inventario=ninventario)

    componentes = Componentes.objects.all().filter(tipo_maquina=maquina.tipo_maquina)
    movimientos = maquina.maquina_poblacion.all().order_by('-fecha_movimiento')[:1]
    incidencias = maquina.incidencias.all()
    grupos_componentes = GrupoComponentes.objects.all()
    mantenimiento_maquinaria = MantenimientoMaquinaria.objects.all().filter(numero_maquina=maquina.id)
    movimientosObra = maquina.obra.all().order_by('-fecha_movimiento')[:1]

    return render(request,
                  'UPR/detail.html',
                  {'maquina': maquina,
                   'ninventario': ninventario,
                   'componentes': componentes,
                   'movimientos': movimientos,
                   'incidencias': incidencias,
                   'grupos_componentes': grupos_componentes,
                   'mantenimiento_maquinaria': mantenimiento_maquinaria,
                   'movimientosObra' : movimientosObra
                   })

# --------------- Add_Incidencia --------------- #
def add_incidencia(request, ninventario):
    form = MaquinaIncidenciasForm(request.POST or None, request.FILES or None)
    maquina = get_object_or_404(Maquina.objects.select_related(
                                            'tipo_maquina','capataz_responsable',
                                        ).prefetch_related('incidencias').order_by('indicencias__fecha'),
                                numero_inventario=ninventario)

    grupos_componentes = GrupoComponentes.objects.all().order_by('position_grupo_componentes')
    componentes = Componentes.objects.all().filter(grupo_componentes__id=1)
    print(componentes)

    if request.method == "POST":
        if form.is_valid():
            # Create, but don't save the new incidencia instance.
            instance = form.save(commit=False)
            # Save the new instance.
            instance.save()
            maquina.incidencias.add(instance)
            maquina.save()
            # Flash message
            messages.success(request, "Incidencia creada.")
            # Redirect
            return HttpResponseRedirect(reverse('upr:maquina_detail', kwargs={'ninventario':ninventario}))
        else:
            messages.error(request, "Error creando la incidencia.")

    return render(request,
              'UPR/incidencias.html',
              {'maquina': maquina,
               'ninventario': ninventario,
               'grupos_componentes': grupos_componentes,
               'form': form
               })

# --------------- Ajax: Get all componentes from a specific Group --------------- #
def get_components_by_group(request):
    grupo_comp_id = request.GET.get('grupo_comp_id', '0')
    componentes = Componentes.objects.all().filter(grupo_componentes__id=grupo_comp_id)
    data = serializers.serialize('json', componentes)
    return HttpResponse(data, content_type="application/json")


# --------------- Add_Ubicacion --------------- #
def add_ubicacion(request, ninventario):
    form = MovimientoMaquinariaForm(request.POST or None, request.FILES or None)
    maquina = get_object_or_404(Maquina.objects.select_related(
                                            'tipo_maquina','capataz_responsable',
                                        ).prefetch_related('maquina_poblacion').order_by('maquina_poblacion__fecha_movimiento'),
                                numero_inventario=ninventario)

    movimientos = maquina.maquina_poblacion.all().order_by('-fecha_movimiento')
    poblacion = Poblacion.objects.all()
    print(poblacion)

    if request.method == "POST":
        if form.is_valid():
            # Create, but don't save the new ubicacion instance.
            instance = form.save(commit=False)
            # Save the new instance.
            instance.save()
            maquina.maquina_poblacion.add(instance)
            maquina.save()
            # Flash message
            messages.success(request, "Ubicación añadida.")
            # Redirect
            return HttpResponseRedirect(reverse('upr:maquina_detail', kwargs={'ninventario':ninventario}))
        else:
            messages.error(request, "Error añadiendo la ubicación.")

    return render(request,
              'UPR/ubicacion.html',
              {'maquina': maquina,
               'ninventario': ninventario,
               'poblacion': poblacion,
               'movimientos': movimientos,
               'form': form
               })


# --------------- Add_Obra --------------- #
def add_obra(request, ninventario):
    form = MovimientoObraForm(request.POST or None, request.FILES or None)
    maquina = get_object_or_404(Maquina.objects.select_related(
                                            'tipo_maquina','capataz_responsable',
                                        ).prefetch_related('obra').order_by('obra__fecha_movimiento'),
                                numero_inventario=ninventario)

    movimientos = maquina.obra.all().order_by('-fecha_movimiento')
    obra = Obra.objects.all()
    print(obra)

    if request.method == "POST":
        if form.is_valid():
            # Create, but don't save the new ubicacion instance.
            instance = form.save(commit=False)
            # Save the new instance.
            instance.save()
            maquina.obra.add(instance)
            maquina.save()
            # Flash message
            messages.success(request, "Obra cambiada.")
            # Redirect
            return HttpResponseRedirect(reverse('upr:maquina_detail', kwargs={'ninventario':ninventario}))
        else:
            messages.error(request, "Error cambiando la obra.")

    return render(request,
              'UPR/obra.html',
              {'maquina': maquina,
               'ninventario': ninventario,
               'obra': obra,
               'movimientos': movimientos,
               'form': form
               })