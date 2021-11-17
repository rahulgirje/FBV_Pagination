from django.db import models

class User(models.Model):
    username = models.CharField( max_length = 150)
    first_name = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150)
