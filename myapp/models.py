from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    mail=models.CharField (max_length=200,unique=True)
    password=models.CharField(max_length=100,unique=True)
    phone=models.IntegerField(default='',unique=True)



class form(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)


class employe(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    mail=models.CharField (max_length=200,unique=True)
    password=models.CharField(max_length=100,unique=True)
    phone=models.IntegerField(default='',unique=True)
    