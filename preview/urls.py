from django.urls import path

from . import views
app_name = 'preview'
urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('home/', views.home, name='home'),


]