from django.shortcuts import render
from .models import Room,Message
# Create your views here.


def ChatHome(request):
    data = Room.objects.all()
    context={
        'data':data
    }
    return render(request,'chat.html',context)


def room(request, room_name):
    room = Room.objects.get(slug=room_name)
    message = Message.objects.filter(room=room)
    context = {
        "room_name": room_name,
        'room':room,
        'message':message
    }
    return render(request, "room.html", context)
