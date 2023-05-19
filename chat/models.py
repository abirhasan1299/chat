from django.db import models
import datetime
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200)
    time = models.DateTimeField(datetime.datetime.now())

    def __str__(self):
        return self.name
class Message(models.Model):
    room = models.ForeignKey(Room,related_name='message',on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

