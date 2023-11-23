from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import createuserform,adduserform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Hey you back")
            return redirect('home')
        else:
            messages.success(request,"sorry unable to login")
            return redirect('home')
    else:       
        return render(request,"home.html",{'records':records})

def login_user(request):
    pass
def logout_user(request):
    logout(request)
    messages.success(request,"see you soon ...")
    return redirect('home')

def register_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username,password=password1)
            user.save()
            messages.success(request,"sucessfully Register now you can login..")
            return redirect('home')
        else:
            messages.success(request,"password mismatch")
            return redirect('register')
    form = createuserform()
    return render(request,'register.html',{'form' : form})


def customer_records(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'customer' : customer_record})
    else:
        messages.success(request,"you must be logged in ")
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        customer_record.delete()
        messages.success(request,"Record deleted successfully ")
        return redirect('home')
    else:
        messages.success(request,"you must be logged in ")
        return redirect('home')

def add_record(request):
    form = createuserform()    
    return render(request,'add_user.html',{'form':form})