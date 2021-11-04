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


# class Event:
#     def __init__(self, id, title, image, location, date, time, attendees, like_number, share_number, description):
#         self.id = id
#         self.title = title
#         self.image = image
#         self.location = location
#         self.date = date
#         self.time = time
#         self.attendees = attendees
#         self.like_number = like_number
#         self.share_number = share_number
#         self.description = description
#
#
# event1 = Event(
#     1,
#     "Bird Watchers",
#     "img/events/bird-watchers.jpg",
#     "Location: Trail A",
#     "09/01/2021",
#     "10:00 AM",
#     "3",
#     "22",
#      "0",
#     "Welcome to the Bird Watchers! If you are a nature lover who wants to get out with like-minded people for "
#     "a day of adventure and fun while seeing and learning about nature. Then this is the group for you."
#     " Can you imagine the thrill of a Bald Eagle soaring over your head? It's an unbelievable feeling! "
#     "Seeing your first hummingbird in the wild is a moment that you would cherish for a lifetime! "
#     "We will be traveling inside different parts of Great Falls for bird watching adventures. "
#     "We only have small groups for a more intimate experience.",
# )
# event2 = Event(
#     2,
#     "Music in the Woods",
#     "img/events/music-in-the-woods.jpg",
#     "Location: Trail B",
#     "09/11/2021",
#     "10:00 AM",
#     "41",
#     "12",
#     "13",
#     "to be add",
# )
# event3 = Event(
#     3,
#     "Deer-patrol",
#     "img/events/deer-patrol.jpeg",
#     "Location: Trail C",
#     "09/21/2021",
#     "10:00 AM",
#     "23",
#     "21",
#     "33",
#     "to be add",
# )
# events = []
#
regular_user = {"username": "alice", "password": "hokie"}
admin_user = {"username": "admin", "password": "admin"}
