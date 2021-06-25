from django.db import models


class register(models.Model):
    first_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    avatar = models.FileField()


