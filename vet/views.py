from django.shortcuts import render
from . import forms
from .forms import UsuarioForm
from .models import Usuario

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html',context)


def signup(request):
    form = forms.UsuarioForm
    return render(request, 'sessions/signup.html', {'form': form})  

def create_user(request):
    form = UsuarioForm(request.POST)
    if form.is_valid():
        form.save()
        

def SingleUsuario(request):
    model = Usuario

