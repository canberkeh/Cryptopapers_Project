from django.urls import path
from . import views

app_name = 'whitepapers'

urlpatterns = [
    path('', views.whitepapers_index, name='whitepapers_index'),
]
