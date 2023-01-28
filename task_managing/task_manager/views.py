from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def home(request):
    return render(request,"index.html")


def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("The user has logged In")
    form =AuthenticationForm()
    context = {'form': form}
    return render(request,'login.html',context=context)



def register(request):
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("The user is registered")
    form=NewUserForm()
    context={'form':form}
    return render(request,'register.html',context=context)

