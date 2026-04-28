from django.shortcuts import render
from .models import Curso

def cursos_view(request):
    cursos = Curso.objects.all()
    return render(request, 'escola/cursos.html', {'cursos': cursos})