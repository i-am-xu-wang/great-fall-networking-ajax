import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from great_fall_events import settings


class Event(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default="img/events/default_event.jpg")
    location = models.CharField(max_length=200)
    date = models.CharField(default="11/10/2021", max_length=30)
    time = models.CharField(default="11:00 AM", max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    organizer = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attendees = models.IntegerField(default=0)
    like_number = models.IntegerField(default=0)
    share_number = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events:event-detail', args=[self.id])


class Account(models.Model):
    title = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    age = models.IntegerField(default=20)
    group = models.CharField(max_length=50)
    intro = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default="img/profile/anonymous-user.png")

# regular_user = {"username": "alice", "password": "hokie"}
# admin_user = {"username": "admin", "password": "admin"}
