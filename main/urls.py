from django.urls import path
from . import views


urlpatterns = [
    path("" , views.index, name='index'),
    path("add_employee", views.add_employee, name='add_employee'),
    path("oops", views.oops, name='oops'),     
]