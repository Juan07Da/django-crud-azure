from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante
from .forms import EstudianteForm

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/lista.html', {'estudiantes': estudiantes})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = EstudianteForm()
    return render(request, 'estudiantes/formulario.html', {'form': form})

def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    form = EstudianteForm(request.POST or None, instance=estudiante)
    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'estudiantes/formulario.html', {'form': form})

def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('lista')
    return render(request, 'estudiantes/confirmar_eliminar.html', {'estudiante': estudiante})
