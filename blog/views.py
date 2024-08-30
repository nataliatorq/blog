# blog/views.py
from django.shortcuts import render
from .models import GostosPessoais, Curiosidades, SobreMim

def home(request):
    gostos_pessoais = GostosPessoais.objects.all()
    curiosidades = Curiosidades.objects.all()
    context = {
        'gostos_pessoais': gostos_pessoais,
        'curiosidades': curiosidades
    }
    return render(request, 'blog/home.html', context)

def sobre(request):
    sobre_mim = SobreMim.objects.first()  # Pegando a primeira instância
    context = {
        'sobre_mim': sobre_mim
    }
    return render(request, 'blog/sobre.html', context)
