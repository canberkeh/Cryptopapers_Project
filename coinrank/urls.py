from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'coinrank'

urlpatterns = [
    path('', views.coinrankindex, name='coinrankindex'),
    # path('like/', views.like_update, name='update'),
]