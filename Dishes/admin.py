from django.contrib import admin
from .models import Food, Dish_Type, Drink_Type, Drinks

# Register your models here.
admin.site.register(Dish_Type)
admin.site.register(Drink_Type)
admin.site.register(Food)
admin.site.register(Drinks)