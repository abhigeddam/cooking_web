from django.db import models
from django.contrib.auth.models import User

class Person_food(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    last_reciepe1 = models.CharField(max_length=128,blank=True)
    last_reciepe2 = models.CharField(max_length=128,blank=True)
    last_reciepe3 = models.CharField(max_length=128,blank=True)

class Cusines(models.Model):
    cusine = models.CharField(max_length=128)

class Diet(models.Model):
    diet = models.CharField(max_length=128)

class Intolerences(models.Model):
    avoid = models.CharField(max_length=128)

class Favaorites(models.Model):
    name = models.CharField(max_length=99999999999)
    image = models.CharField(max_length=99999999999)
    ids = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Reciepes(models.Model):
    name = models.CharField(max_length=99999999)
    image = models.ImageField(upload_to='user_recipes/')
    steps = models.CharField(max_length=99999999999)
    user_id = models.ForeignKey(User,blank=True, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0,blank=True)
    
