from django import forms
from departamentos.models import Departamento


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'
