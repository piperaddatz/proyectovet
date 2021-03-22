from django import forms
from . import models


class UsuarioForm(forms.ModelForm):
    class Meta:
        fields = ('username','email','password')
        model = models.Usuario

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'})
        }

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Nombre'
        self.fields['email'].label = 'Email'





