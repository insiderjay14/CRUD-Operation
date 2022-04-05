from django.db import models

# Create your models here.

class register(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.BigIntegerField()
    li=[['MALE','male'],['FEMALE','female']]
    gender=models.CharField(max_length=10,choices=li)