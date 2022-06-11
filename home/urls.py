
from django.urls import path
from home import views



urlpatterns = [
    path('index',views.index),
    path('home',views.home,name='hh'),
    path('contact',views.contact,name='cc'),
    path('about',views.about,name='aa'),
]