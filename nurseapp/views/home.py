from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from nurseapp.forms import *
from .records import record_eval_function


def error403(request):
    """
    Vista que devuelve la pagina de error 403
    """
    return render(request, "403.html")


@login_required
def home2(request):
    """
    Vista que procesa la solicitud de visualizar el menu principal
    Presenta contadores de objetos segun el usuario logueado
    """
    lista = {}
    if request.user.is_superuser:
        patients = Patient.objects.all()
        lista.update({'patients': Patient.objects.all().count()})
        lista.update({'records': Record.objects.all().count()})
    else:
        lista.update({'patients': Patient.objects.filter(nurse_id=request.user.id).count()})
        lista.update({'records': Record.objects.filter(patient__nurse_id=request.user.id).count()})
        patients = Patient.objects.filter(nurse_id=request.user.id)

    records = []
    objects = []
    for p in patients:
        records.append(Record.objects.filter(patient__cid=p.cid).order_by('date').last())

    records = record_eval_function(records)

    for r in records:
        #if r.status_pressure != "Normal" or r.status_bpm != "Normal":
            objects.append(r)

    return render(request, "home2.html",
                  {'lista': lista, 'objects': objects})
