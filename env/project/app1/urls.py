
from django.urls import path,include
from .views import Home,About,Readme,Add_some,Edit,Delete

urlpatterns = [
    path('',Home ,name='home'),
    path('about/',About ,name='about'),
    path('read/',Readme,name='read_data'),
    path('add/',Add_some,name="add_data"),
    path('edit/',Edit,name="edit_data"),
    path('delete/', Delete, name="delete_data"),



]