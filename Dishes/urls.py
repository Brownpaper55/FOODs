from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView




urlpatterns = [path('', views.IndexView.as_view(), name ='Home' ),
               path('foods', views.FoodsListView.as_view(), name='foods'),
               path('drinks', views.DrinksListView.as_view(), name='Drinks'),
               path('login', LoginView.as_view(template_name='login.html'), name = 'login'),
               path('logout', LogoutView.as_view(template_name='logout.html'), name = 'logout'),
               path('signup', views.SignupFormView.as_view(), name= 'signup'),
               path('success/', views.FormSuccesView.as_view(), name= 'success'),
               path('buy/<int:pk>/', views.buy, name='buy')
               
               ]
