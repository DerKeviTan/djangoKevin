from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Constructora
    path('constructoras/', views.listar_constructoras, name='constructoras_list'),
    path('constructoras/nueva/', views.crear_constructora, name='crear_constructora'),
    path('constructoras/editar/<int:pk>/', views.editar_constructora, name='editar_constructora'),
    path('constructoras/eliminar/<int:pk>/', views.eliminar_constructora, name='eliminar_constructora'),

    # ProyectoInfraestructura
    path('proyectos/', views.listar_proyectos, name='proyectos_list'),
    path('proyectos/nuevo/', views.crear_proyecto, name='crear_proyecto'),
    path('proyectos/editar/<int:pk>/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/eliminar/<int:pk>/', views.eliminar_proyecto, name='eliminar_proyecto'),

    # Carretera
    path('carreteras/', views.listar_carreteras, name='carreteras_list'),
    path('carreteras/nueva/', views.crear_carretera, name='crear_carretera'),
    path('carreteras/editar/<int:pk>/', views.editar_carretera, name='editar_carretera'),
    path('carreteras/eliminar/<int:pk>/', views.eliminar_carretera, name='eliminar_carretera'),

    # Presupuesto
    path('presupuestos/', views.listar_presupuestos, name='presupuestos_list'),
    path('presupuestos/nuevo/', views.crear_presupuesto, name='crear_presupuesto'),
    path('presupuestos/editar/<int:pk>/', views.editar_presupuesto, name='editar_presupuesto'),
    path('presupuestos/eliminar/<int:pk>/', views.eliminar_presupuesto, name='eliminar_presupuesto'),
]

