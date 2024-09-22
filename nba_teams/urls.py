from django.urls import path
from . import views

app_name = 'nba_teams'

urlpatterns = [
    path('<int:team_id>/', views.team_page, name='team_page'),
]