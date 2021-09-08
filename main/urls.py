from django.urls import path
from . import views


urlpatterns = [
    path("" , views.index, name='index'),
    path("add_employee", views.add_employee, name='add_employee'),
    path("filter/<int:id>", views.category, name='filter'),
    path("edufilter/<int:id>", views.category_2, name='edufilter'),
    path("oops", views.oops, name='oops'), 
    path("show_detail/<int:id>", views.show_detail, name='show_detail'),
    path("delete/<int:id>", views.delete, name='delete'),
    path("update_page/<int:pk>", views.update_page, name='update_page'),
    path("sorting", views.sorting, name='sorting'),
    path("sorting_1", views.sorting_1, name='sorting_1'),  
    path("search", views.search, name='search'),
]