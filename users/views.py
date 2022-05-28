from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def profiles(request):
    return render(request, 'users/profiles.html')

def loginPage(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        try:
            # check if user exist
            user = User.objects.get(username=username)
        except:
            print('[username] not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # create session for user
            login(request, user)
            return redirect('profiles')
        else:
            print('username or password is incorrect')
    return render(request, 'users/login_registry.html')

def logoutPage(request):
    logout(request, )
    return redirect('login')
