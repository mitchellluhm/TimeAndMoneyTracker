from django.conf.urls import url
from TimeMoneyApp import views

app_name = "TimeMoneyApp"

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^user_register/', views.user_register, name='user_register'),
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    url(r'^time_event/', views.time_event, name='time_event'),
    url(r'^time_event_visualize/', views.time_event_visualize, name='time_event_visualize'),
]
