from django.conf.urls import url
from TimeMoneyApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/', views.user, name='user'),
]