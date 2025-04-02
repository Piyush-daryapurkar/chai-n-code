
from django.urls import path,include
from .views import Home,About

urlpatterns = [
    path('',Home ,name='home'),
    path('about/',About ,name='about'),

]
