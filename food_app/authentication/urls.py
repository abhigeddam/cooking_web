from django.urls import path 
from .views import register,logins,logouts,check
urlpatterns = [ 
    path('register/',register,name='register'),
    path('login/',logins,name='logins'),
    path('logout/',logouts,name = 'logout'),
    path('check/',check,name = 'check'),
    ]