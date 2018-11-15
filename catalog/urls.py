from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='catalog_home'),
    path('category/<category_slug>/', views.show_category, name='catalog_category'),
    path('product/<product_slug>', views.show_product, name='catalog_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
