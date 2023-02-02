from django import forms

class SimpleForm(forms.Form):
    nombre = forms.CharField(label='Tu nombre', max_length=100)
    apellido_1 = forms.CharField(max_length=255)
    email = forms.EmailField()
    pwd = forms.CharField(max_length=255)
