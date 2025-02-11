from django import forms
from .models import Constructora, ProyectoInfraestructura, Carretera, Presupuesto

class ConstructoraForm(forms.ModelForm):
    class Meta:
        model = Constructora
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProyectoInfraestructuraForm(forms.ModelForm):
    class Meta:
        model = ProyectoInfraestructura
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'constructora': forms.Select(attrs={'class': 'form-control'}),
        }

class CarreteraForm(forms.ModelForm):
    class Meta:
        model = Carretera
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'longitud': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'proyecto': forms.Select(attrs={'class': 'form-control'}),
        }

class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = '__all__'
        widgets = {
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_aprobacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'proyecto': forms.Select(attrs={'class': 'form-control'}),
        }
