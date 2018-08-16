from django import forms
from django.contrib.auth.models import User
from TimeMoneyApp.models import UserProfileInfo, TimeEvent

class NewUserForm(forms.ModelForm):
    '''
    New user sign up form
    '''

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    '''
    Currently not used
    '''

    class Meta():
        model = UserProfileInfo
        fields = ()
        
class TimeEventForm(forms.ModelForm):
    '''
    Begin a time event
    '''

    class Meta():
        model = TimeEvent
        fields = ('event_name', 'event_type', 'event_start')

class TimeEventEndForm(forms.ModelForm):
    '''
    @TODO : make by_id optional field
    '''

    # Uniqie ID to update event_end time stamp
    by_id = forms.CharField()

    class Meta():
        model = TimeEvent
        fields = ('by_id', 'event_end',)
