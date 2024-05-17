from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, FormView, View
from .models import Food, Drinks
from .forms import Signup, Foodlist

# Create your views here.

class IndexView(TemplateView):
    template_name = 'home.html'


class FoodsListView(ListView):
    model = Food
    template_name = 'food.html'
    context_object_name = 'Food'
    

def buy(request, pk):
    buy_food = get_object_or_404(Food, pk=pk)
    return render(request, 'buy.html', {'food': buy_food})

    

    #else:
     #   form = Foodlist()
    #turn render(request, 'food.html',{'form': form})


class DrinksListView(ListView):
    model = Drinks
    template_name = 'Drinks.html'
    context_object_name = 'Drink'


class SignupFormView(FormView):
    template_name = 'signup.html'
    form_class = Signup
    success_url = 'success/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FormSuccesView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("user created successfully")





    
    