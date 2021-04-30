from django.urls import path
from . import views

app_name = 'coinrank'

urlpatterns = [
    path('', views.coinrankindex, name='coinrankindex'),
    path('create_new_coin', views.create_new_coin, name='create_new_coin'),
    path('coinrank/<str:id>/like', views.like_counter, name='like_counter'),
    path('coinrank/<str:id>/dislike', views.dislike_counter, name='dislike_counter'),
    path('coinrank/<str:id>/hodler', views.hodler_counter, name='hodler_counter'),
]