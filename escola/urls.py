from django.urls import path
from . import views

urlpatterns = [
    path('', views.cursos_view, name='cursos'),
]