from django.shortcuts import render, redirect
from .models import Produs
from django.db import IntegrityError

# Create your views here.

def homepage(request):
    lista_produse = Produs.objects.all()
    return render(request, 'homepage.html',{'lista_produse': lista_produse})

def adauga(request):
    if request.method=="POST":
        nume_produs = request.POST.get('nume')
        try:
            Produs.objects.create(nume=nume_produs)
            mesaj = f"Ai adaugat produsul {nume_produs}"
        except IntegrityError:
            mesaj = f"Produsul {nume_produs} exista deja"
        return render(request, 'adauga_produs.html', {'mesaj':mesaj})
    return render(request, 'adauga_produs.html')

def cumpara(request, produs_id):
    produs = Produs.objects.get(id = produs_id)
    produs.cumparat = True
    produs.save()
    return redirect('homepage')

def sterge(request, produs_id):
    produs = Produs.objects.get(id = produs_id)
    produs.delete()
    return redirect('homepage')






