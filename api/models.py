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

    patient_unique_name = models.CharField(max_length=5000)
    age = models.PositiveIntegerField(default=0)
    details = models.CharField(max_length=5000)
    join_date = models.DateTimeField('Join published', default='2011-11-11 11:11')


class Doctor(models.Model):
    def __str__(self):
        return self.user.username

    doctor_age = models.CharField(max_length=5000)
    doctor_age = models.PositiveIntegerField(default=0)
    doctor_details = models.CharField(max_length=5000)
    patient_name = models.IntegerField()


class Pharmacist(models.Model):
    def __str__(self):
        return self.user.username

    pharmacist_name = models.CharField(max_length=5000)
    pharmacist_age = models.PositiveIntegerField(default=0)
    pharmacist_details = models.CharField(max_length=5000)
    patient_name = models.IntegerField()
