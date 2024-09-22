from nba_api.live.nba.endpoints import scoreboard
import pprint
import requests
from bs4 import BeautifulSoup
from nba_teams.models import *


# get today's game scores
def get_scores():
    # Today's Score Board
    games = scoreboard.ScoreBoard()
    results = scoreboard.ScoreBoard().games.get_dict()

    return results


def get_team_image(team_id, team_name):
    #   Check for team image in database
    team_logo = EasternConferenceTeams.objects.filter(team_id=team_id).first()

    if team_logo:
        return team_logo.team_logo_url
    else:
        team_logo = WesternConferenceTeams.objects.filter(team_id=team_id).first()
        return team_logo.team_logo_url
