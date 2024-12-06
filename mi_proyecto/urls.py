from django.contrib import admin
from django.urls import path
from tareas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_tareas, name='lista_tareas'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
]
urlpatterns += [
    path('editar/<int:pk>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar/<int:pk>/', views.eliminar_tarea, name='eliminar_tarea'),
]


