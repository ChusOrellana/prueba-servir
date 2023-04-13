from django.views import generic
from django.urls import reverse_lazy
from departamentos.models import Departamento
from departamentos.forms import DepartamentoForm


class DepartamentoListView(generic.ListView):
    model = Departamento
    template_name = 'departamentos/departamento/list.html'


class DepartamentoCreateView(generic.CreateView):
    model = Departamento
    form_class = DepartamentoForm
    success_url = reverse_lazy('departamentos:listar_departamentos')
    template_name = 'departamentos/departamento/form.html'


class DepartamentoUpdateView(generic.UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    success_url = reverse_lazy('departamentos:listar_departamentos')
    template_name = 'departamentos/departamento/form.html'


class DepartamentoDeleteView(generic.DeleteView):
    model = Departamento
    success_url = reverse_lazy('departamentos:listar_departamentos')
    template_name = 'departamentos/departamento/delete.html'
