# blog/views.py
from django.shortcuts import render
from .models import GostosPessoais, Curiosidades, SobreMim

def home(request):
    gostos_pessoais = GostosPessoais.objects.all()
    curiosidades = Curiosidades.objects.all()
    return render(request, 'blog/home.html', {
        'gostos_pessoais': gostos_pessoais,
        'curiosidades': curiosidades
    })

def sobre(request):
    sobre_mim = SobreMim.objects.first()  # Pegando a primeira instância
    return render(request, 'blog/sobre.html', {
        'sobre_mim': sobre_mim
    })

