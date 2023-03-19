from django.db import models

class Person(models.Model):
    username = models.CharField(max_length=38)
    password = models.CharField(max_length=24)
