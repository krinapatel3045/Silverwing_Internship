from django.urls import path
from .views import home_new

app_name = 'Home_new'

urlpatterns=[
    path('',home_new,name='Home_new'),
    
]