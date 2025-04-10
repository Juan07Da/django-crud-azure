from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_estudiantes, name='lista'),
    path('nuevo/', views.crear_estudiante, name='crear'),
    path('editar/<int:pk>/', views.editar_estudiante, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar_estudiante, name='eliminar'),
]
