from django.db import models

# Create your models here.
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.db import IntegrityError
import datetime


class Patient(models.Model):
    nurse = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    genders = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=genders)
    cid = models.IntegerField(unique=True)
    birth = models.DateField()
    age = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return '%s %s' % (self.name, self.lastname)


class Record(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    # date = models.DateField(default=datetime.date.today)
    date = models.DateTimeField(default=datetime.datetime.now)
    pressure1 = models.IntegerField()
    pressure2 = models.IntegerField()
    bpm = models.IntegerField()
    status_pressure = models.CharField(max_length=10, default='', blank=True)
    status_bpm = models.CharField(max_length=10, default='', blank=True)

    # vitals = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return 'for %s %s' % (self.patient.name, self.patient.lastname)


class RangeP1(models.Model):
    pressure1_min = models.IntegerField()
    pressure1_max = models.IntegerField()
    level = models.IntegerField(unique=True)
    status = models.CharField(max_length=25)


class RangeP2(models.Model):
    pressure2_min = models.IntegerField()
    pressure2_max = models.IntegerField()
    level = models.IntegerField(unique=True)
    status = models.CharField(max_length=25)


class RangeB(models.Model):
    age = models.IntegerField()
    genders = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=genders)
    bpm_min = models.IntegerField()
    bpm_max = models.IntegerField()
    status = models.CharField(max_length=25)


class Range(models.Model):
    age = models.IntegerField()
    genders = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=genders)
    bpm_min = models.IntegerField()
    bpm_max = models.IntegerField()
    pressure1_min = models.IntegerField()
    pressure1_max = models.IntegerField()
    pressure2_min = models.IntegerField()
    pressure2_max = models.IntegerField()
