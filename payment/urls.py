from django.urls import path
from . import views
app_name = 'payment'
urlpatterns = [
    path('', views.payment_process, name='payment_process'),
    path('', views.payment_canceled, name='payment_canceled'),
    path('', views.payment_done, name='payment_done'),
]