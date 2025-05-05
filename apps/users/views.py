from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.users.forms import CustomUserCreationForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully registered.')
            return redirect('index')
        else:
            messages.error(request, 'Registration error.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful , Welcome back!')
            return redirect('index')
        else:
            messages.error(request, 'Login error.')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})



@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out.')
    return redirect('login')



def index(request):
    return render(request, 'bookmodule/index.html')