from django.shortcuts import render
from Trabajo.models import familiar

def vista_familiar (request):
    lista_familiar = familiar.objects.all()
    return render(request, "Trabajo/familiares.html", {"lista_familiar": lista_familiar})

# Create your views here.
