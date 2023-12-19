from django.urls import path
from . import views

app_name = 'nba_today'

urlpatterns = [

    path('', views.nba_results, name='nba_results'),
    path('game-leaders/<int:num>/', views.game_leaders, name='game_leaders')
]