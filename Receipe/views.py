from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
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
       
        data = request.POST
       
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES['receipe_image']
       
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





