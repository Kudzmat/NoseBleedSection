from django.urls import path
from . import views

app_name = 'nba_stats'

urlpatterns = [

    path('player-search/', views.player_search, name='player_search'),
    path('player-comparison-search/', views.compare_players, name='compare_players'),
    path('graph-comparison/', views.show_graph, name='show_graph'),
    path('player-comparison-profiles/', views.compare_profiles, name='compare_profiles'),
    path('player-career-page/<str:player_full_name>/<str:player_id>/', views.player_details, name='player_details'),
    path('regular-season-totals/<str:player_full_name>/<str:player_id>/', views.regular_season, name='regular_season'),
    path('post-season-totals/<str:player_full_name>/<str:player_id>/', views.post_season, name='post_season'),
    path('regular-season-rankings/<str:player_full_name>/<str:player_id>/', views.regular_season_rankings, name='regular_season_rankings'),
    path('post-season-rankings/<str:player_full_name>/<str:player_id>/', views.post_season_rankings, name='post_season_rankings')
]