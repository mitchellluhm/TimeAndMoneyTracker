from django.db import models
from django.contrib.auth.models import User
import django.utils
import datetime
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    email = models.EmailField(max_length=254, unique=True)
    total_events = models.IntegerField(default=0)
    total_expenses = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class TimeEvent(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING) # TODO : add on_delete
    event_name = models.CharField(max_length=256, default="Unnamed Event")
    event_type = models.CharField(max_length=256, default="Unspecified Event Type")
    event_start = models.DateTimeField(default=django.utils.timezone.now)
    event_end = models.DateTimeField(null=True)

    def __str__(self):
        return "Some Time Event"

    # TODO : compute length of event with methods
    def get_event_duration(self):

        if self.event_end:
            diff = self.event_end - self.event_start
            #return diff.total_seconds()
        else:
            #now = datetime.datetime.utcnow().replace(tzinfo='US/Eastern') 
            #diff = now - self.event_start
            #return -1.0
            diff = 60.0
            return "Ongoing"
        return str(diff / 60.0)

# TODO : add MoneyEvent
