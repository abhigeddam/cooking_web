from django.urls import path
from .views import Favmanager,Favdisp,account,deletefav
urlpatterns = [
    path('favoratie/',Favmanager,name='favoratie'),
    path('favdisp/',Favdisp,name='Fav'),
    path('account/',account,name='Acc'),
    path('favoratie/del',deletefav,name='Favdel')
]