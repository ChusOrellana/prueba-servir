from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from empleados.models import Empleado
from empleados.forms import EmpleadoForm


def index(request):
    return render(request, 'index.html')


class EmpleadoListView(generic.ListView):
    model = Empleado
    template_name = 'empleados/empleado/list.html'


class EmpleadoCreateView(generic.CreateView):
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados:listar_empleados')
    template_name = 'empleados/empleado/form.html'


class EmpleadoUpdateView(generic.UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados:listar_empleados')
    template_name = 'empleados/empleado/form.html'


class EmpleadoDeleteView(generic.DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados:listar_empleados')
    template_name = 'empleados/empleado/delete.html'
