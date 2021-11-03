from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    user_form = UserCreationForm()
    profile_form = ProfileForm()
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()

            profile_form = ProfileForm(request.POST, instance=user.profile)
            if profile_form.is_valid():
                profile_form.save()
                login(request, user)
                return redirect('accounts:user-home')
                


    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
        }
    return render(request, 'register.html', context)
    
    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('accounts:user-home')
        else:
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('products:home')

@login_required
def edit_profile(request):
        if request.method == 'POST':
            username_change_form = UsernameChangeForm(data=request.POST, instance=request.user)
            profile_form = ProfileForm(data=request.POST, instance=request.user.profile)
            if username_change_form.is_valid() and profile_form.is_valid():
                username_change_form.save()
                profile_form.save()
                return redirect ('accounts:user-home')
        else:
            username_change_form = UsernameChangeForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)


        context = {
            'username_change_form' : username_change_form,
            'profile_form' : profile_form,
        }

        return render(request, 'edit_profile.html', context)

def user_home(request):
    context = {}
    return render(request, 'user_home.html', context)


