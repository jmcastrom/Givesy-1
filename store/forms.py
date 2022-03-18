from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder':"Tu nombre"
    }))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder':"Tu correo"
    }))
    pswd = forms.CharField(max_length=100, widget=forms.PasswordInput())


class ProductForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder':"Tu nombre"
    }))
    descripcion = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder':"Tu nombre"
    }))
    images = forms.ImageField()
