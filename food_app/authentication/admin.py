from django.contrib import admin
from food_app.models import Cusines,Diet,Intolerences,Person_food
admin.site.register(Cusines,Diet,Intolerences,Person_food)
