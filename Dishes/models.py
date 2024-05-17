from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique= True)
    email = models.EmailField(unique= True)
    


class Dish_Type(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self) :
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Dish_Type, on_delete=models.CASCADE)
    price = models.FloatField()
    

    def __str__(self) :
        return self.name

class Drink_Type(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self) :
        return self.name

    

class Drinks(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Drink_Type, on_delete= models.CASCADE)
    price = models.FloatField()
    

    def __str__(self) :
        return self.name



