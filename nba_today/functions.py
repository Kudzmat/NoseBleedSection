from nba_api.live.nba.endpoints import scoreboard
import pprint
import requests
from bs4 import BeautifulSoup
import base64
import numpy as np
from io import BytesIO


# get today's game scores
def get_scores():
    # Today's Score Board
    games = scoreboard.ScoreBoard()
    results = scoreboard.ScoreBoard().games.get_dict()

    return results

    # pprint.pprint(results[0]['awayTeam'])


def get_team_image(team_id):
    #  the image will be attained from this url
    url = f'https://www.nba.com/team/{team_id}'

    # Make an HTTP GET request to the URL
    response = requests.get(url)
    # response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the team image tag within the appropriate element and class
    logo_tag = soup.find('img', {'class': 'TeamLogo_logo__PclAJ TeamHeader_logo__rRnWF'})

    # finding the team logo using src
    if logo_tag:
        team_logo = logo_tag['src']
        return team_logo

    return None


#results = get_scores()
# pprint.pprint(results)
# pprint.pprint(game_results)
# team_id = game_results[0]['awayTeam']['teamId']



# game['teamLogo'] = logo
# print(logo"""
# print(logos)

# denver = get_team_image("1610612743")
# print(denver)
"""
for game in results:
    home_team = game['homeTeam']['teamName']
    home_team_id = game['homeTeam']['teamId']
    home_team_logo = get_team_image(home_team_id)

    away_team = game['awayTeam']['teamName']
    away_team_id = game['awayTeam']['teamId']
    away_team_logo = get_team_image(away_team_id)

    print(f"{home_team}: {home_team_logo} vs {away_team} {away_team_logo}")
    print()
"""