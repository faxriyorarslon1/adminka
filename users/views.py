from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegisterForm, LoginForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout 


# Create your views here.
def register_view(request):
    form=UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context={
        "form":form
    }

    return render(request, template_name = 'auth/page-register.html', context=context)


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
    context={
        "form":form
    }
    return render(request, template_name = 'auth/page-login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/')


def profile_view(request):
    profile = request.user.profile.first()
    return render(request, 'profile.html', context={"profile":profile})

