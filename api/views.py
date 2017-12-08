from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from . import models
from api.forms import SignUpForm

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            user = authenticate(username=username, password=raw_password)
            if form.cleaned_data.get('select') == 'Patient':
                patientinfo = models.PatientInfo(user=user, patient_unique_name=username,
                                                 details=str(first_name + ' additional_info ' + last_name))

                patientinfo.save()
            elif form.cleaned_data.get('select') == 'Doctor':
                doctorinfo = models.Doctor(user=user, doctor_name=username,
                                           doctor_details=str(first_name + ' additional_info ' + last_name))

                doctorinfo.save()
            elif form.cleaned_data.get('select') == 'Pharmacist':
                pharmacistinfo = models.Doctor(user=user, pharmacist_name=username,
                                               pharmacist_details=str(first_name + ' additional_info ' + last_name))

                pharmacistinfo.save()
            login(request, user)

            return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'api/signup.html', {'form': form})


def home(request):
    return render(request, 'api/home.html')
