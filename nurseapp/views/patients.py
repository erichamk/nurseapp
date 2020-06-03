from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from nurseapp.forms import *
import datetime
from django.contrib import messages


# PLANTILLAS
@login_required
@permission_required('nurseapp.view_patient', raise_exception=True)
def adm_patient(request):
    """
    Vista que procesa la solicitud de visualizar y eliminar patients
    """
    if request.user.is_superuser:
        objects = Patient.objects.all()
    else:
        objects = Patient.objects.filter(nurse_id=request.user.id)


    today = datetime.date.today()

    for o in objects:
        o.age = today.year - o.birth.year - ((today.month, today.day) < (o.birth.month, o.birth.day))

    return render(request, "abm/patients.html", {'objects': objects})


@login_required
@permission_required('nurseapp.add_patient', raise_exception=True)
def adm_patient_add(request):
    """
    Vista que procesa la solicitud de crear patients
    """
    mensaje = ''
    if request.method == 'POST':
        if request.POST.get("save"):
            form = PatientForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.nurse = User.objects.get(pk=request.user.id)
                instance.save()
                mensaje = 'Patient \"' + instance.__str__() + '\" created'
                messages.add_message(request, messages.INFO, mensaje)
                # Log.objects.create(fecha=datetime.datetime.now(), usuario=request.user, accion="Crea patient \'"+instance.__str__()+"\'")
                return redirect("/patients/")
            else:
                print(form.errors)
                print('invalid')
        else:
            return redirect("/patients/")
    else:
        form = PatientForm(initial={'birth': '2000-01-01'})

    return render(request, "abm/patients/add.html", {'form': form, 'mensaje': mensaje})


@login_required
@permission_required('nurseapp.change_patient', raise_exception=True)
def adm_patient_mod(request):
    """
    Vista que procesa la solicitud de modificar patients
    """
    mensaje = ''
    if request.method == 'POST':
        if request.POST.get("edit"):
            if request.POST.get("object_id"):
                p = Patient.objects.get(pk=request.POST['object_id'])
                form = PatientForm(instance=p)
                object_id = request.POST.get("object_id")
                return render(request, "abm/patients/edit.html", {'object_id': object_id, 'form': form, 'mensaje': mensaje})
            else:
                return redirect("/patients/")

        elif request.POST.get("save"):
            object_id = request.POST.get("object_id")
            p = Patient.objects.get(pk=request.POST['object_id'])
            form = PatientForm(request.POST, instance=p)
            if form.is_valid():
                instance = form.save()
                # Log.objects.create(fecha=datetime.datetime.now(), usuario=request.user, accion="Modifica patient \'" + instance.__str__() + "\'")
                mensaje = 'Patient saved'
                messages.add_message(request, messages.INFO, mensaje)
                return redirect("/patients/")
            else:
                print(form.errors)
                print('invalid')
        else:
            return redirect("/patients/")

    else:
        return redirect("/patients/")



@login_required
@permission_required('nurseapp.change_patient', raise_exception=True)
def adm_patient_del(request):
    """
    Vista que procesa la solicitud de eliminar patients
    """

    mensaje = ''
    if request.method == 'POST':
        if request.POST.get('object_id'):
            instance = Patient.objects.get(pk=request.POST['object_id'])
            if request.POST.get('delete'):
                form = PatientForm(instance=instance)
                for key in form.fields.keys():
                    if form.fields.get(key):
                        form.fields[key].widget.attrs['readonly'] = True
                return render(request, "abm/patients/delete.html",
                              {'form': form, 'object_id': request.POST.get('object_id')})
            if request.POST.get('delete_confirm'):
                instance = Patient.objects.get(pk=request.POST['object_id'])
                instance.delete()
                mensaje = 'Patient deleted'
                messages.add_message(request, messages.INFO, mensaje)

    return redirect("/patients/")
