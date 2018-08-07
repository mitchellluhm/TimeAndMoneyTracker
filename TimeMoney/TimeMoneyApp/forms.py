from django import forms
from django.contrib.auth.models import User
from TimeMoneyApp.models import UserProfileInfo, TimeEvent

class NewUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ()
        
class TimeEventForm(forms.ModelForm):

    '''
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(TimeEventForm, self).__init__(*args, **kwargs)
        '''

    class Meta():
        model = TimeEvent
        fields = ('event_name', 'event_type')
