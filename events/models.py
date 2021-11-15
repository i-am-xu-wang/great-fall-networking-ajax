import datetime

from django.db import models

# Create your models here.
from great_fall_events import settings


class Event(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default="img/events/default_event.jpg")
    location = models.CharField(max_length=200)
    date = models.CharField(default="11/10/2021", max_length=30)
    time = models.CharField(default="11:00 AM", max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    organizer = models.CharField(max_length=30)
    attendees = models.IntegerField(default=0)
    like_number = models.IntegerField(default=0)
    share_number = models.IntegerField(default=0)
    description = models.TextField(blank=True)


class User(models.Model):
    title = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    age = models.IntegerField(default=20)
    group = models.CharField(max_length=50)
    intro = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default="img/profile/anonymous-user.png")


regular_user = {"username": "alice", "password": "hokie"}
admin_user = {"username": "admin", "password": "admin"}
