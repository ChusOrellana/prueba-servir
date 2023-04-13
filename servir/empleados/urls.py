from django.urls import path
from empleados import views

app_name = 'empleados'

urlpatterns = [
    path('', views.index, name='index'),
    path('empleado/list', views.EmpleadoListView.as_view(), name='listar_empleados'),
    path('empleado/crear', views.EmpleadoCreateView.as_view(), name='crear_empleado'),
    path('empleado/<pk>/editar', views.EmpleadoUpdateView.as_view(), name='editar_empleado'),
    path('empleado/<pk>/delete', views.EmpleadoDeleteView.as_view(), name='delete_empleado'),
]
