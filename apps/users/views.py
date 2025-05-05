from django.shortcuts import render ,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


#Task1 LAB12

# Task 1: Register View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم التسجيل بنجاح.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Task 2: Custom Login View
class CustomLoginView(LoginView):
    template_name = 'users/login.html'

# Task 3: Custom Logout View
class CustomLogoutView(LogoutView):
    next_page = 'login'

# Task 4: Example of protected view
@login_required
def protected_view(request):
    return render(request, 'users/protected.html')

