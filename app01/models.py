from django.db import models

# Create your models here.

class Staff(models.Model):
    name=models.CharField(max_length=32)
    position=models.CharField(max_length=32)


class Account(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
