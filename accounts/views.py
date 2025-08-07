from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ClinicForm, ClinicLoginForm
from .models import Clinic
from django.contrib.auth.models import User

def register_clinic(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        clinic_form = ClinicForm(request.POST)
        if user_form.is_valid() and clinic_form.is_valid():
            user = user_form.save()
            login(request, user)
            clinic = clinic_form.save(commit=False)
            clinic.user = user
            clinic.save()
            return redirect('dashboard')
    else:
        user_form = UserRegistrationForm()
        clinic_form = ClinicForm()
    return render(request, 'accounts/clinic_register.html', {
        'user_form': user_form,
        'clinic_form': clinic_form
    })

def login_clinic(request):
    if not User.objects.exists():
        return redirect('register_clinic') 

    if request.method == 'POST':
        form = ClinicLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = ClinicLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_clinic(request):
    logout(request)
    return redirect('login_clinic')

@login_required
def dashboard(request):
    try:
        clinic = Clinic.objects.get(user=request.user)
    except Clinic.DoesNotExist:
        return redirect('register_clinic')  # if no clinic exists, go to register
    return render(request, 'accounts/dashboard.html', {'clinic': clinic})
