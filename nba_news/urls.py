from django.urls import path
from . import views

app_name = 'nba_news'

urlpatterns = [

    path('the-ringer/', views.the_ringer_news, name='ringer_news'),
]