from django import forms
# from datetimewidget.widgets import DateWidget, TimeWidget, DateTimeWidget
import datetime
from .models import *
# from .widgets import SelectTimeWidget
from django import forms
from django.db.models import Q


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['nurse', 'age']
        labels = {
            'name': 'Name',
            'lastname': 'Last-name',
            'gender': 'Gender',
            'cid': 'ID',
            'birth': 'Date of birth'
        }
        widgets = {
            'birth': forms.SelectDateWidget(years=range(1900, 2021)),
        }


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
        exclude = ['date', 'status_bpm', 'status_pressure', 'vitals']
        labels = {
            'patient': 'Patient',
            'pressure1': 'Systolic Blood Pressure',
            'pressure2': 'Diastolic Blood Pressure',
            'bpm': 'BPM',
        }
        widgets = {
            #'date': forms.DateTimeInput(),
            #'datet': forms.SelectDateWidget(years=range(1900, 2021)),

        }

        def clean_status_pressure(self):
             data = self.cleaned_data['password']
             return data

class RangeForm(forms.ModelForm):
    class Meta:
        model = Range
        fields = '__all__'
        labels = {
            'pressure1_min': 'Min. Systolic Blood Pressure',
            'pressure2_min': 'Min. Diastolic Pressure',
            'pressure1_max': 'Max. Systolic Blood Pressure',
            'pressure2_max': 'Max. Diastolic Pressure',
            'bpm_min': 'Min. BPM',
            'bpm_max': 'Max. BPM',
        }
class RangeP1Form(forms.ModelForm):
    class Meta:
        model = RangeP1
        fields = '__all__'
        labels = {
            'pressure1_min': 'Min. Systolic Blood Pressure',
            'pressure1_max': 'Max. Systolic Blood Pressure',
            'level': 'Scale level',
        }
class RangeP2Form(forms.ModelForm):
    class Meta:
        model = RangeP2
        fields = '__all__'
        labels = {
            'pressure2_min': 'Min. Diastolic Pressure',
            'pressure2_max': 'Max. Diastolic Pressure',
            'level': 'Scale level',
        }
class RangeBForm(forms.ModelForm):
    class Meta:
        model = RangeB
        fields = '__all__'
        labels = {
            'bpm_min': 'Min. BPM',
            'bpm_max': 'Max. BPM',
        }
