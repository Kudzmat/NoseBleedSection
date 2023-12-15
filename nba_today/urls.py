from django.urls import path
from . import views

app_name = 'nba_today'

urlpatterns = [

    path('', views.nba_results, name='nba_results'),
]