from django import forms
from empleados.models import Empleado


class EmpleadoForm(forms.ModelForm):
    codigo = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}), required=False)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)

    class Meta:
        model = Empleado
        fields = '__all__'
