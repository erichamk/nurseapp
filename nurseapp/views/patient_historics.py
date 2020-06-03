from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from nurseapp.forms import *
from .records import record_eval_function


def patient_historics(request):
    """
    Vista que procesa la solicitud de visualizar y eliminar records
    """
    search = ''
    message = ''
    name = ''
    objects = {}
    print(request)
    if request.GET.get('search'):
        search = request.GET.get('search')
        objects = Record.objects.filter(patient__cid=request.GET.get("search")).order_by('date')
        if objects:
            name = objects.first().patient.name + ' ' + objects.first().patient.lastname
            objects = record_eval_function(objects)
        else:
            message = 'Not found...'

    return render(request, "patient_historics.html",
                  {'objects': objects, 'message': message, 'name': name, 'search': search})
