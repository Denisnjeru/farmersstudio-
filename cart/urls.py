from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.show_cart, name='show_cart')
]
