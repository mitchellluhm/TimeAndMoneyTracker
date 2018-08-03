from django import forms
from django.contrib.auth.models import User
from TimeMoneyApp.models import UserProfileInfo

class NewUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = '__all__'
        
