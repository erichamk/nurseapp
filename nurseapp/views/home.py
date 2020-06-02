from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from nurseapp.forms import *

def error403(request):
    """
    Vista que devuelve la pagina de error 403
    """
    return render(request,"403.html")


@login_required
def home2(request):
    """
    Vista que procesa la solicitud de visualizar el menu principal
    Presenta contadores de objetos segun el usuario logueado
    """
    lista={}
    lista.update({'patients':Patient.objects.all().count()})
    lista.update({'records':Record.objects.all().count()})
    return render(request,"home2.html",
                  {'lista': lista})
