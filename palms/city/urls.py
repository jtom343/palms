from django.urls import path
from . import views

app_name = 'city'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('allcities/',views.allcities,name='allcities'),
    ]

import random

def create_lottery_numbers():
    values = set() #initializing an empty setself.
    while len(values) < 6: #will run until you achieve 6 numbers in the set.
        values.add(random.randint(1,20))
    return values

print(create_lottery_numbers())
