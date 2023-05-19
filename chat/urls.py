from django.urls import path
from .views import ChatHome,room
urlpatterns = [
    path('',ChatHome,name="chathome"),
    path("<str:room_name>/", room, name="room"),
]
