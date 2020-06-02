from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from nurseapp.forms import *
import datetime
from django.contrib import messages


# PLANTILLAS
@login_required
@permission_required('nurseapp.view_record', raise_exception=True)
def adm_record(request):
    """
    Vista que procesa la solicitud de visualizar y eliminar records
    """
    objects = Record.objects.all()

    today = datetime.date.today()

    for o in objects:
        o.patient.age = today.year - o.patient.birth.year - (
                (today.month, today.day) < (o.patient.birth.month, o.patient.birth.day))

        range1 = RangeP1.objects.filter(pressure1_min__lte=o.pressure1, pressure1_max__gte=o.pressure1).last()
        range2 = RangeP2.objects.filter(pressure2_min__lte=o.pressure2, pressure2_max__gte=o.pressure2).last()
        range3 = RangeB.objects.filter(gender=o.patient.gender, age__gte=o.patient.age, bpm_min__lte=o.bpm,
                                       bpm_max__gte=o.bpm).order_by(
            'age').last()
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
            o.status_bpm = range3.status
        else:
            o.status_bpm = 'N/A'

    return render(request, "abm/records.html", {'objects': objects})


@login_required
@permission_required('nurseapp.add_record', raise_exception=True)
def adm_record_add(request):
    """
    Vista que procesa la solicitud de crear records
    """
    mensaje = ''
    if request.method == 'POST':
        if request.POST.get("save"):
            form = RecordForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)

                instance.save()
                mensaje = 'Record \"' + instance.__str__() + '\" created successfully!'
                messages.add_message(request, messages.INFO, mensaje)
                # Log.objects.create(fecha=datetime.datetime.now(), usuario=request.user, accion="Crea record \'"+instance.__str__()+"\'")

                return redirect("/records/")

            else:
                print(form.errors)
                print('invalid')
        else:
            return redirect("/records/")
    else:
        form = RecordForm()

    return render(request, "abm/records/add.html", {'form': form, 'mensaje': mensaje})


@login_required
@permission_required('nurseapp.change_record', raise_exception=True)
def adm_record_mod(request):
    """
    Vista que procesa la solicitud de modificar records
    """
    mensaje = ''
    if request.method == 'POST':
        if request.POST.get("edit"):
            if request.POST.get("object_id"):
                p = Record.objects.get(pk=request.POST['object_id'])
                form = RecordForm(instance=p)
                object_id = request.POST.get("object_id")
                return render(request, "abm/records/edit.html",
                              {'object_id': object_id, 'form': form, 'mensaje': mensaje})
            else:
                return redirect("/records/")

        elif request.POST.get("save"):
            object_id = request.POST.get("object_id")
            p = Record.objects.get(pk=request.POST['object_id'])
            form = RecordForm(request.POST, instance=p)
            if form.is_valid():
                instance = form.save()
                # Log.objects.create(fecha=datetime.datetime.now(), usuario=request.user, accion="Modifica record \'" + instance.__str__() + "\'")
                mensaje = 'Record modified successfully!'
                messages.add_message(request, messages.INFO, mensaje)
                return redirect("/records/")
            else:
                print(form.errors)
                print('invalid')
        else:
            return redirect("/records/")

    else:
        return redirect("/records/")


@login_required
@permission_required('nurseapp.change_record', raise_exception=True)
def adm_record_del(request):
    """
    Vista que procesa la solicitud de eliminar records
    """

    mensaje = ''
    if request.method == 'POST':
        if request.POST.get('object_id'):
            instance = Record.objects.get(pk=request.POST['object_id'])
            if request.POST.get('delete'):
                form = RecordForm(instance=instance)
                for key in form.fields.keys():
                    if form.fields.get(key):
                        form.fields[key].widget.attrs['readonly'] = True
                return render(request, "abm/records/delete.html",
                              {'form': form, 'object_id': request.POST.get('object_id')})
            if request.POST.get('delete_confirm'):
                instance = Record.objects.get(pk=request.POST['object_id'])
                instance.delete()
                mensaje = 'Record deleted successfully!'
                messages.add_message(request, messages.INFO, mensaje)

    return redirect("/records/")
