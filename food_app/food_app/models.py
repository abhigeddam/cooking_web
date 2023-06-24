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
    description = models.CharField(max_length=999999)
    user_id = models.ForeignKey(User,blank=True, on_delete=models.CASCADE,related_name='recipes')
    upvotes = models.IntegerField(default=0,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
class Trending(models.Model):
    item = models.CharField(max_length=99999999)
    ids = models.IntegerField(default=0,blank=True)
    image = models.CharField(max_length=99999999999)
    time = models.DateTimeField(auto_now_add=True)

class Trend_container(models.Model):
    ids = models.IntegerField(default=0,blank=True)
    image = models.CharField(max_length=99999999999)
    item = models.CharField(max_length=99999999)
    views = models.IntegerField(default=1,blank=True)