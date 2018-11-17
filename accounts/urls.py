from  django.urls import path , include
from economic import settings
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('my_account/', views.my_account, name='my_account'),
   # path('order_details/', views.orderdetails, name='order_details'),
   # path('order_info/', views.orderinfo, name='order_info'),
    path('login/', auth_views.auth_login(), name='login'),
]

