from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm, CreateTask, UpdateUser
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Task, Profile
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='login')
def delete_user(request):
    if request.method=='POST':
        user=User.objects.get(id=request.user.id)
        user.delete()
        return redirect('dashboard')
    user = User.objects.get(id=request.user.id)
    context={'form':user}
    return render(request,'delete_user.html',context=context)

@login_required(login_url='login')
def profile_update(request):
    if request.method=='POST':
        form=UpdateUser(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    form=UpdateUser(instance=request.user)
    context={'form':form}
    return render(request,'profile_update.html',context=context)


@login_required(login_url='login')
def DeleteTask(request,pk):
    if request.method=='POST':
        task=Task.objects.get(id=pk)
        task.delete()
        return redirect('view_task')
    task = Task.objects.get(id=pk)
    context={'task':task}
    return render(request,'delete_task.html',context=context)


@login_required(login_url='login')
def UpdateTask(request,pk):
    if request.method=='POST':
        task = Task.objects.get(id=pk)
        form = CreateTask(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    task=Task.objects.get(id=pk)
    form=CreateTask(instance=task)
    context={'form':form}
    return render(request,'update_task.html',context=context)

    context={'task':task}
    return render(request,'view_task.html',context=context)

@login_required(login_url='login')
def ViewTask(request):
    current_user=request.user.id
    task=Task.objects.all().filter(user=current_user)
    context={'task':task}
    return render(request,'view_task.html',context=context)

@login_required(login_url='login')
def NewTask(request):
    if request.method=='POST':
        form=CreateTask(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
            return redirect("dashboard")
    form=CreateTask()
    context={'form':form}
    return render(request,'create_task.html',context=context)

@login_required(login_url='login')
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
            current_user=form.save(commit=False)
            form.save()
            messages.success(request,"User registration was successful!")
            return redirect('login')
    form=NewUserForm()
    context={'form':form}
    return render(request,'register.html',context=context)

