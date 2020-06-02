from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from nurseapp.forms import *
import datetime
from django.contrib import messages


# PLANTILLAS
@login_required
@permission_required('nurseapp.view_range', raise_exception=True)
def adm_range(request):
    """
    Vista que procesa la solicitud de visualizar y eliminar ranges
    """
    objects = RangeP1.objects.all()
    objects2 = RangeP2.objects.all()
    objects3 = RangeB.objects.all()

    return render(request, "abm/ranges.html", {'objects': objects, 'objects2': objects2, 'objects3': objects3})


@login_required
@permission_required('nurseapp.add_range', raise_exception=True)
def adm_range_add(request):
    """
    Vista que procesa la solicitud de crear ranges
    """
    message = ''
    range_type = ''
    if request.method == 'POST':
        if request.POST.get("save"):

            if request.POST.get("type") == "p1":
                form = RangeP1Form(request.POST)
            if request.POST.get("type") == "p2":
                form = RangeP2Form(request.POST)
            if request.POST.get("type") == "b":
                form = RangeBForm(request.POST)

            if form.is_valid():
                instance = form.save()
                message = 'Range created successfully!'
                messages.add_message(request, messages.INFO, message)
                # Log.objects.create(fecha=datetime.datetime.now(), usuario=request.user, accion="Crea range \'"+instance.__str__()+"\'")
                return redirect("/ranges/")
            else:
                print(form.errors)
                print('invalid')
        else:
            return redirect("/ranges/")
    else:
        if request.GET.get("add"):
            range_type = request.GET.get("add")
            if range_type == 'p1':
                form = RangeP1Form()
            elif range_type == 'p2':
                form = RangeP2Form()
            elif range_type == 'b':
                form = RangeBForm()
        else:
            return redirect("/ranges/")

    return render(request, "abm/ranges/add.html", {'form': form, 'message': message, 'type': range_type})


@login_required
@permission_required('nurseapp.change_range', raise_exception=True)
def adm_range_mod(request):
    """
    Vista que procesa la solicitud de modificar ranges
    """
    message = ''
    range_type = ''
    if request.method == 'POST':
        if request.POST.get("edit"):
            range_type = request.POST.get("edit")
            if range_type == "p1":
                p = RangeP1.objects.get(pk=request.POST['object_id'])
                form = RangeP1Form(instance=p)
                object_id = request.POST.get("object_id")
                return render(request, "abm/ranges/edit.html",
                              {'object_id': object_id, 'form': form, 'message': message, 'type': range_type})
            if range_type == "p2":
                p = RangeP2.objects.get(pk=request.POST['object_id'])
                form = RangeP2Form(instance=p)
                object_id = request.POST.get("object_id")
                return render(request, "abm/ranges/edit.html",
                              {'object_id': object_id, 'form': form, 'message': message, 'type': range_type})
            if range_type == "b":
                p = RangeB.objects.get(pk=request.POST['object_id'])
                form = RangeBForm(instance=p)
                object_id = request.POST.get("object_id")
                return render(request, "abm/ranges/edit.html",
                              {'object_id': object_id, 'form': form, 'message': message, 'type': range_type})
            else:
                return redirect("/ranges/")

        elif request.POST.get("save"):
            object_id = request.POST.get("object_id")

            if request.POST.get("type") == "p1":
                p = RangeP1.objects.get(pk=request.POST['object_id'])
                form = RangeP1Form(request.POST, instance=p)
            if request.POST.get("type") == "p2":
                p = RangeP2.objects.get(pk=request.POST['object_id'])
                form = RangeP2Form(request.POST, instance=p)
            if request.POST.get("type") == "b":
                p = RangeB.objects.get(pk=request.POST['object_id'])
                form = RangeBForm(request.POST, instance=p)

            if form.is_valid():
                instance = form.save()
                # Log.objects.create(fecha=datetime.datetime.now(), usuario=request.user, accion="Modifica range \'" + instance.__str__() + "\'")
                message = 'Range modified successfully!'
                messages.add_message(request, messages.INFO, message)
                return redirect("/ranges/")
            else:
                print(form.errors)
                print('invalid')
        else:
            return redirect("/ranges/")
    else:
        return redirect("/ranges/")


@login_required
@permission_required('nurseapp.change_range', raise_exception=True)
def adm_range_del(request):
    """
    Vista que procesa la solicitud de eliminar ranges
    """
    range_type = ''
    message = ''
    if request.method == 'POST':
        if request.POST.get('delete'):
            range_type = request.POST.get("delete")
            if range_type == "p1":
                instance = RangeP1.objects.get(pk=request.POST['object_id'])
                form = RangeP1Form(instance=instance)
            if range_type == "p2":
                instance = RangeP2.objects.get(pk=request.POST['object_id'])
                form = RangeP2Form(instance=instance)
            if range_type == "b":
                instance = RangeB.objects.get(pk=request.POST['object_id'])
                form = RangeBForm(instance=instance)
            for key in form.fields.keys():
                if form.fields.get(key):
                    form.fields[key].widget.attrs['readonly'] = True
            return render(request, "abm/ranges/delete.html",
                          {'form': form, 'object_id': request.POST.get('object_id'), 'type': range_type})

        if request.POST.get('delete_confirm'):
            if request.POST.get("type") == "p1":
                instance = RangeP1.objects.get(pk=request.POST['object_id'])
            if request.POST.get("type") == "p2":
                instance = RangeP2.objects.get(pk=request.POST['object_id'])
            if request.POST.get("type") == "b":
                instance = RangeB.objects.get(pk=request.POST['object_id'])
            instance.delete()
            message = 'Range deleted successfully'
            messages.add_message(request, messages.INFO, message)

    return redirect("/ranges/")
