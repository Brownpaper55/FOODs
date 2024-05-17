from django import forms
from django.contrib.auth.forms import UserCreationForm 
from .models import CustomUser, Food

class Signup(UserCreationForm):
    email = forms.EmailField(max_length=100, required= True)
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')


class Foodlist(forms.Form):
    items = forms.ModelChoiceField(queryset=Food.objects.all(), empty_label=None)
    
