from django.shortcuts import render
from django.http import HttpResponse
# from TimeMoneyApp.models import User
from TimeMoneyApp.forms import NewUserForm


# Create your views here.
def index(request):
    return render(request, 'TimeMoneyApp/index.html')

def user(request):
    
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            print("Form is valid")
            form.save(commit=True)
            index(request)

    return render(request, 'TimeMoneyApp/user.html', { 'form' : form })
    
