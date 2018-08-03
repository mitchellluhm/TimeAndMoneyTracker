from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    email = models.EmailField(max_length=254, unique=True)
    total_events = models.IntegerField(default=0)
    total_expenses = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class TimeEvent:

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING) # TODO : add on_delete
    event_name = models.CharField(max_length=256, default="Unnamed Event")
    event_type = models.CharField(max_length=256, default="Unspecified Event Type")
    event_start = models.DateTimeField(auto_now=True)
    event_end = models.DateTimeField(null=True)

    def __str__(self):
        return self.event_name + " of type " + self.event_type

    # TODO : compute length of event with methods

# TODO : add MoneyEvent
