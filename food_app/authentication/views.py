from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .form import CreateUserForm
from database.models import Profile
import datetime

# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        response = CreateUserForm(request.POST)
        if response.is_valid():
            x = response.save()
            y = Profile(user=x)
            y.save()
            messages.success(request, "registration successful")
            redirect('logins')
        else:
            messages.error(request, "password must contain 8 charecters and a special character")
    context = {'form':form}
    return render(request,'register.html',context)

def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            request.session['user'] = user.get_username()
            request.session['id'] = user.id
            profile = Profile.objects.get(user__id=user.id)
            if (profile.last_login.day < datetime.datetime.now().day) or (profile.last_login.month < datetime.datetime.now().month):
                profile.searches_left = 5
                profile.save()
    
            username = user.get_username()

            return redirect('api_searchs')
        else:
            messages.error(request,'password or username is incorrect')
            print('oopss')
            return redirect('logins')
    return render(request,'login.html',{'register':'register'})
def logouts(request):
    logout(request)
    return redirect('logins')

def check(request):
    return render(request,'new.html')
