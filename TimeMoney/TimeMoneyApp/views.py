from django.shortcuts import render
from TimeMoneyApp.forms import NewUserForm, UserProfileInfoForm, TimeEventForm, TimeEventEndForm
from TimeMoneyApp.models import TimeEvent
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
import time

# Create your views here.
def index(request):
    return render(request, 'TimeMoneyApp/index.html')

def user_register(request):
    
    registered = False

    if request.method == 'POST':
        user_form = NewUserForm(data=request.POST)
        # profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid(): # and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

         # profile = profile_form.save(commit=False)
         # profile.user = user
         # profile.save()

            registered = True
        else:
            print(user_form.errors) #profile_form.errors)

    else:
        user_form = NewUserForm()
        # profile_form = UserProfileInfoForm()

    return render(request, 'TimeMoneyApp/user_register.html',
                  { 
                   'user_form' : user_form,
                   # 'profile_form' : profile_form,
                   'registered' : registered
                  }
                 )
    
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active.")
        else:
            print("Someone tried to login and failed.")
            #return HttpResponse("Invalid login credentials")
            return render(request, 'TimeMoneyApp/invalid_login.html', {})
    else:
        return render(request, 'TimeMoneyApp/user_login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def time_event(request):
    # Create context dictionary of their active events
    user_event_list = TimeEvent.objects.filter(user=request.user)

    form = TimeEventForm()
    last_event = TimeEvent.objects.order_by('event_start').last()
    print(last_event.get_event_duration())
    form_end = TimeEventEndForm(instance=last_event)

    if request.method == 'POST':
        # Check first form
        form = TimeEventForm(request.POST)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.user = request.user
            #form.save(commit=True)
            form_save.save()
            return index(request)
        else:
            print("Some Form Error in time_event")

        # Check second form
        form_end = TimeEventEndForm(request.POST, instance=last_event)
        if form_end.is_valid():
            # print('Form by_id: ' + str(form_end['by_id'].value()))
            new_inst = TimeEvent.objects.get(id=form_end['by_id'].value())
            form_end = TimeEventEndForm(request.POST, instance=new_inst)
            form_save = form_end.save(commit=False)
            #form_save.user = request.user
            #form.save(commit=True)
            form_save.save()
            return index(request)
        else:
            print("Some Form Error in time_event")

    return render(request, 'TimeMoneyApp/time_event.html',
                  { 'form' : form,
                    'form_end' : form_end,
                    'user_event_list' : user_event_list,
                  })

@login_required
def time_event_visualize(request):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    user_event_list = TimeEvent.objects.filter(user=request.user)

    eventX_durationY = {}
    n = 0

    for ue in user_event_list:
        time_str = ue.get_event_duration()
        time_str = time_str.split('.')[0]
        time_splt = time.strptime(time_str.split(',')[0],'%H:%M:%S')
        secs = datetime.timedelta(hours=time_splt.tm_hour,
                                  minutes=time_splt.tm_min,
                                  seconds=time_splt.tm_sec).total_seconds()
        mins = secs / 60.0
        eventX_durationY[n] = mins
        print(eventX_durationY[n])
        d = pd.Series(data=eventX_durationY)

        p = sns.barplot(d)
        f = p.get_figure()
        f.savefig('hi.png')
        

        ''' TODO MAKE DATA STRUCT WITH MINS AND DATES '''
        ''' SEND THAT TO GRAPH MAKER '''

        n += 1

    return render(request, 'TimeMoneyApp/time_event_visualize.html',
                  { 'user_event_list' : user_event_list, })
