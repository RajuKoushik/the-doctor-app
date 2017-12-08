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

            user = authenticate(username=username, password=raw_password)
            if form.cleaned_data.get('select') == 'Patient':
                patientinfo = models.PatientInfo(user=user)
                patientinfo.save()
            login(request, user)

            return redirect('home')


    else:
        form = SignUpForm()
    return render(request, 'api/signup.html', {'form': form})


def home(request):
    return render(request, 'api/home.html')
