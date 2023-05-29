from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from .models import *

def Receipe(request):

    if request.method == 'POST':
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES['receipe_image']

        Receipes.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )  

      
     
    queryset = Receipes.objects.all()
    context = {'receipe':queryset}

    return render(request , 'receipe.html',context)

def update_receipe(request , id):

    queryset = Receipes.objects.get(id = id)

    if request.method == "POST":
  
           
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
       
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipe/')


    context = {'receipes':queryset}
    return render(request , 'update_receipe.html',context)

def delete_receipe(request,id):
    queryset = Receipes.objects.get(id=id)
    queryset.delete()
    
    return redirect('/receipe/')



def login_page(request):
    if request.method == "POST":

        data = request.POST

        if not User.objects.filter(username = data.get('username')).exists():
            messages.error(request, "Invalid Username")
            return redirect ('/login/')
        
        user = authenticate(username = data.get('username') , password = data.get('password'))

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect('/receipe/')

    return render(request, 'login.html')

def logout_page(request):
        logout(request)
        return redirect('/login/')


def Register(request):

    if request.method == "POST":
       
       data = request.POST
       
       user = User.objects.filter(username  = data.get('username'))
       if user.exists():
           messages.info(request, "UserName already Taken.")
           return redirect('/register/')

       
       firstname = request.POST.get('firstname')
       lastname = request.POST.get('lastname')
       username = request.POST.get('username')
       password = request.POST.get('password')

       user =  User.objects.create(
           first_name  = firstname,
           last_name = lastname,
           username = username,
           
       ) 
       user.set_password(password)
       user.save()
       messages.info(request, "Account Created Successfully")
       return redirect('/register/')

    return render(request, 'register.html')

