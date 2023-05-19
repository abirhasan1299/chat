from django.shortcuts import render,redirect
from chat.models import Room
import datetime

def HOME(request):
    return redirect("chathome")

def createRm(request):
    if request.method=="POST":
        name = request.POST['name']
        slug = request.POST['slug']
        time = datetime.datetime.now()
        obj = Room(name = name,slug=slug,time=time)
        obj.save()
        return redirect('home')
    return render(request,'create_room.html')