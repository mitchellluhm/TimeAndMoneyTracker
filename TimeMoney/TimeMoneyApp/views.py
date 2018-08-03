from django.shortcuts import render
from TimeMoneyApp.forms import NewUserForm, UserProfileInfoForm

# Create your views here.
def index(request):
    return render(request, 'TimeMoneyApp/index.html')

def register(request):
    
    registered = False

    if request.method == 'POST':
        user_form = NewUserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = NewUserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'TimeMoneyApp/user.html',
                  { 
                   'user_form' : user_form,
                   'profile_form' : profile_form,
                   'registered' : registered
                  }
                 )
    
