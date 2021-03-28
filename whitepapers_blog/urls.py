from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'whitepapers_blog'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
]