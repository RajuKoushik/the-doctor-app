from datetime import datetime
from django.db import models
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone


class PatientInfo(models.Model):
    def __str__(self):
        return self.user.username

    patient_unique_name = models.CharField(max_length=5000, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(default=0)
    details = models.CharField(max_length=5000, null=True)



class Doctor(models.Model):
    def __str__(self):
        return self.user.username

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
    doctor_name = models.CharField(max_length=5000,null=True)
    doctor_details = models.CharField(max_length=5001)
    doctor_tame = models.CharField(max_length=5000, null=True)
    patient = models.ForeignKey(PatientInfo,null=True)


class Pharmacist(models.Model):
    def __str__(self):
        return self.user.username

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
    pharmacist_name = models.CharField(max_length=5000)
    pharmacist_age = models.PositiveIntegerField(default=0)
    pharmacist_details = models.CharField(max_length=5000)
    patient = models.ForeignKey(PatientInfo,null=True)
