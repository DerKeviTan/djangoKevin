from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Constructora, ProyectoInfraestructura, Carretera, Presupuesto
from .forms import ConstructoraForm, ProyectoInfraestructuraForm, CarreteraForm, PresupuestoForm

# Página de inicio
def index(request):
    return render(request, 'base.html')

# ------------------------ CONSTRUCTORA ------------------------

# Listar Constructoras
def listar_constructoras(request):
    constructoras = Constructora.objects.all()
    return render(request, "constructoras_list.html", {"constructoras": constructoras})

# Crear Constructora
def crear_constructora(request):
    if request.method == 'POST':
        form = ConstructoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('constructoras_list'))
    else:
        form = ConstructoraForm()
    return render(request, "crear_constructora.html", {"form": form})

# Editar Constructora
def editar_constructora(request, pk):
    constructora = get_object_or_404(Constructora, pk=pk)
    if request.method == 'POST':
        form = ConstructoraForm(request.POST, instance=constructora)
        if form.is_valid():
            form.save()
            return redirect(reverse('constructoras_list'))
    else:
        form = ConstructoraForm(instance=constructora)
    return render(request, "editar_constructora.html", {"form": form})

# Eliminar Constructora
def eliminar_constructora(request, pk):
    constructora = get_object_or_404(Constructora, pk=pk)
    if request.method == 'POST':
        constructora.delete()
        return redirect(reverse('constructoras_list'))
    return render(request, "eliminar_constructora.html", {"constructora": constructora})

# ------------------------ PROYECTO ------------------------

# Listar Proyectos
def listar_proyectos(request):
    proyectos = ProyectoInfraestructura.objects.all()
    return render(request, "proyectos_list.html", {"proyectos": proyectos})

# Crear Proyecto
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoInfraestructuraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('proyectos_list'))
    else:
        form = ProyectoInfraestructuraForm()
    return render(request, "crear_proyecto.html", {"form": form})

# Editar Proyecto
def editar_proyecto(request, pk):
    proyecto = get_object_or_404(ProyectoInfraestructura, pk=pk)
    if request.method == 'POST':
        form = ProyectoInfraestructuraForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect(reverse('proyectos_list'))
    else:
        form = ProyectoInfraestructuraForm(instance=proyecto)
    return render(request, "editar_proyecto.html", {"form": form})

# Eliminar Proyecto
def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(ProyectoInfraestructura, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect(reverse('proyectos_list'))
    return render(request, "eliminar_proyecto.html", {"proyecto": proyecto})

# ------------------------ CARRETERA ------------------------

# Listar Carreteras
def listar_carreteras(request):
    carreteras = Carretera.objects.all()
    return render(request, "carreteras_list.html", {"carreteras": carreteras})

# Crear Carretera
def crear_carretera(request):
    if request.method == 'POST':
        form = CarreteraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('carreteras_list'))
    else:
        form = CarreteraForm()
    return render(request, "crear_carretera.html", {"form": form})

# Editar Carretera
def editar_carretera(request, pk):
    carretera = get_object_or_404(Carretera, pk=pk)
    if request.method == 'POST':
        form = CarreteraForm(request.POST, instance=carretera)
        if form.is_valid():
            form.save()
            return redirect(reverse('carreteras_list'))
    else:
        form = CarreteraForm(instance=carretera)
    return render(request, "editar_carretera.html", {"form": form})

# Eliminar Carretera
def eliminar_carretera(request, pk):
    carretera = get_object_or_404(Carretera, pk=pk)
    if request.method == 'POST':
        carretera.delete()
        return redirect(reverse('carreteras_list'))
    return render(request, "eliminar_carretera.html", {"carretera": carretera})

# ------------------------ PRESUPUESTO ------------------------

# Listar Presupuestos
def listar_presupuestos(request):
    presupuestos = Presupuesto.objects.all()
    return render(request, "presupuestos_list.html", {"presupuestos": presupuestos})

# Crear Presupuesto
def crear_presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('presupuestos_list'))
    else:
        form = PresupuestoForm()
    return render(request, "crear_presupuesto.html", {"form": form})

# Editar Presupuesto
def editar_presupuesto(request, pk):
    presupuesto = get_object_or_404(Presupuesto, pk=pk)
    if request.method == 'POST':
        form = PresupuestoForm(request.POST, instance=presupuesto)
        if form.is_valid():
            form.save()
            return redirect(reverse('presupuestos_list'))
    else:
        form = PresupuestoForm(instance=presupuesto)
    return render(request, "editar_presupuesto.html", {"form": form})

# Eliminar Presupuesto
def eliminar_presupuesto(request, pk):
    presupuesto = get_object_or_404(Presupuesto, pk=pk)
    if request.method == 'POST':
        presupuesto.delete()
        return redirect(reverse('presupuestos_list'))
    return render(request, "eliminar_presupuesto.html", {"presupuesto": presupuesto})
