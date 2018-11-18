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
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_change/', views.change_password, name='password_change'),
    path('password_change_done/', views.password_change_done, name='password_change_done')
]

