from django.db import models

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=25)
    message = models.CharField(max_length=100)