from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm

USERS = {}

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            mobile = form.cleaned_data['mobile']
            password = form.cleaned_data['password']
            USERS[mobile] = password  
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'api/signup.html', {'form': form})

def login_view(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            mobile = form.cleaned_data['mobile']
            password = form.cleaned_data['password']
            if USERS.get(mobile) == password:
                return render(request, 'api/login_success.html', {'mobile': mobile})
            else:
                error = 'Invalid credentials'
    else:
        form = LoginForm()
    return render(request, 'api/login.html', {'form': form, 'error': error})
