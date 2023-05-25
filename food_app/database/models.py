from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete = models.CASCADE,related_name='Profile')
    image = models.ImageField(upload_to='user_profiles/',null=True, blank=True)
    recipe_shares = models.IntegerField(default=0)
    coins = models.IntegerField(default=0)
    searches_left = models.IntegerField(default=0)
    default_searches = models.IntegerField(default=0)
    following = models.ManyToManyField(User,related_name='followers')

