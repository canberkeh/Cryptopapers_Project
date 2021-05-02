from django.urls import path
from . import views

app_name = 'coinrank'

urlpatterns = [
    path('', views.coinrankindex, name='coinrankindex'),
    path('create_new_coin', views.create_new_coin, name='create_new_coin'),
    path('coinrank/<str:id>/like', views.like_counter, name='like_counter'),
    path('coinrank/<str:id>/dislike', views.dislike_counter, name='dislike_counter'),
    path('coinrank/<str:id>/hodler', views.hodler_counter, name='hodler_counter'),
    path('<str:coin_id>/comments', views.comments, name='comments'),
    path('<str:id>/like', views.comment_like_counter, name='comment_like_counter'),
    path('<str:id>/dislike', views.comment_dislike_counter, name='comment_dislike_counter'),

]