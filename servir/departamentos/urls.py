from django.urls import path
from departamentos import views

app_name = 'departamentos'

urlpatterns = [
    path('departamento/list', views.DepartamentoListView.as_view(), name='listar_departamentos'),
    path('departamento/crear', views.DepartamentoCreateView.as_view(), name='crear_departamento'),
    path('departamento/<pk>/editar', views.DepartamentoUpdateView.as_view(), name='editar_departamento'),
    path('departamento/<pk>/delete', views.DepartamentoDeleteView.as_view(), name='delete_departamento'),
]
