from django.urls import path
from . import views

app_name = 'coinrank'

urlpatterns = [
    path('', views.coinrankindex, name='coinrankindex'),
    path('create_new_coin', views.create_new_coin, name='create_new_coin'),

    # path('like/', views.like_update, name='update'),
]