from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.CharField(max_length=100)
    fullname = models.CharField(max_length=255)
    address = models.CharField(max_length= 150)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length= 15)

