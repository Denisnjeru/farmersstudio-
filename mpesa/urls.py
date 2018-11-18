urls.py

from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^get_end/$',views.CreateEndPoint.as_view(), name = 'create_end' ),
    url(r'^validation/$', csrf_exempt(views.ValidationView.as_view()), name='major'),
    url(r'^confirmation/$', csrf_exempt(views.ConfirmationView.as_view()), name='major'),
]