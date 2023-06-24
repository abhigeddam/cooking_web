from django.urls import path
from .views import Favmanager,Favdisp,Account,Deletefav,Community,addfollowers,Recipe_submission,Shop
urlpatterns = [
    path('favoratie/',Favmanager,name='favoratie'),
    path('favdisp/',Favdisp,name='Fav'),
    path('account/',Account,name='Acc'),
    path('favoratie/del',Deletefav,name='Favdel'),
    path('community/',Community,name='community'),
    path('add_followers',addfollowers,name='add_followers'),
    path('submit/',Recipe_submission,name='Submit'),
    path('shop/',Shop,name='Shop'),
]