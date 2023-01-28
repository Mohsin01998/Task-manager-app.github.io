from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.


def dashboard(request):
    return render(request,'dashboard.html')

def logout_page(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')


def home(request):
    return render(request,"index.html")


def login_page(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
    form =AuthenticationForm()
    context = {'form': form}
    return render(request,'login.html',context=context)



def register(request):
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form=NewUserForm()
    context={'form':form}
    return render(request,'register.html',context=context)

