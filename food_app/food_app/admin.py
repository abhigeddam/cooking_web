from django.contrib import admin
from food_app.models import Cusines,Diet,Intolerences,Person_food,Reciepes,Favaorites,Trending
from database.models import Profile
admin.site.register(Cusines)
admin.site.register(Diet)
admin.site.register(Intolerences)
admin.site.register(Person_food)
admin.site.register(Reciepes)
admin.site.register(Favaorites)
admin.site.register(Trending)
admin.site.register(Profile)