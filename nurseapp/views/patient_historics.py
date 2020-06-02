from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from nurseapp.forms import *


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
            for o in objects:
                range1 = RangeP1.objects.filter(pressure1_min__lte=o.pressure1, pressure1_max__gte=o.pressure1).last()
                range2 = RangeP2.objects.filter(pressure2_min__lte=o.pressure2, pressure2_max__gte=o.pressure2).last()
                range3 = RangeB.objects.filter(gender=o.patient.gender, age__gte=o.patient.age,
                                               bpm_max__gte=o.bpm).order_by('age').last()
                if range1 and range2:
                    # pressure status
                    if range1.level > range2.level:
                        o.status_pressure = range1.status
                    else:
                        o.status_pressure = range2.status
                    # bpm status
                else:
                    o.status_pressure = 'N/A'
                if range3:
                    if o.bpm > range3.bpm_max:
                        o.status_bpm = "High"
                    elif o.bpm < range3.bpm_min:
                        o.status_bpm = "Low"
                    else:
                        o.status_bpm = "Normal"
                else:
                    o.status_bpm = 'N/A'
        else:
            message = 'Not found...'

    return render(request, "patient_historics.html",
                  {'objects': objects, 'message': message, 'name': name, 'search': search})
