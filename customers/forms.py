from django import forms

class ClienteForm(forms.Form):
    dni = forms.CharField(max_length=200, required=True, label='DNI')
    nombre = forms.CharField(max_length=200, required=True, label='Nombre')
    email = forms.EmailField(required=True, label='Email')
    profesion = forms.CharField(max_length=200, required=True, label='Profesión')
    actividad_economica = forms.CharField(max_length=200, required=True, label='Actividad Económica')
    empresa = forms.CharField(max_length=200, required=True, label='Empresa')
    ingresos = forms.IntegerField(required=True, label='Ingresos')
    deudas = forms.IntegerField(required=True, label='Deudas')
    credit_scoring = forms.IntegerField(required=True, label='Credit Scoring')
    cliente_actual = forms.BooleanField(required=False, label='Cliente Actual')
