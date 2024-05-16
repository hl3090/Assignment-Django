"""
Q. What is Django URLs?make program to create django urls
Ans. 
   In Django, URLs are used to map URL patterns to views. This is done using the urls.pyfile, which is located in the 
   root directory of a Django project.
   
   from django.urls import path
   from . import views

   urlpatterns = [
        path('', views.home, name='index'),
        path('login/', views.login, name='login'),
    ]
"""