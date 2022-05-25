from ast import Name
from email.mime import message
import imp
from cv2 import redirectError
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Register
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')

def register(request):
    print(request.method)
    if request.method == "POST":
        name = request.POST['name']
       
        email = request.POST['email']
       # print[email]
        
        password = request.POST['password']
        #printpassword)

        password2 = request.POST['password2']
        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exist')
                return redirect('/register')
            else :
                user = Register(name = name,email =  email,password  = password)
                user.save()
                return redirect('/login')
        # return redirect('/login')
        # messages.success(request, 'You have registered succesfully.')
        else:
            messages.info(request,'Incorrect Password')
            return redirect('/register')
    else:
        return render(request, 'register.html') 
    

    # return render(request, 'register.html',{'form':form})
 
def login(request):
    return render(request, 'login.html')

def contact(request):
    print(request.method)
    if request.method == "POST":
        print(1)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 