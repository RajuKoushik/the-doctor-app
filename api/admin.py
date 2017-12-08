# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from api.models import PatientInfo, Doctor, Pharmacist
# Register your models here.
admin.site.register(PatientInfo)
admin.site.register(Doctor)
admin.site.register(Pharmacist)