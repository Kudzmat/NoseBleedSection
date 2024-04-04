from nba_api.live.nba.endpoints import scoreboard
import pprint
import requests
from bs4 import BeautifulSoup
from .models import TeamLogo


# get today's game scores
def get_scores():
    # Today's Score Board
    games = scoreboard.ScoreBoard()
    results = scoreboard.ScoreBoard().games.get_dict()

    return results

    # pprint.pprint(results[0]['awayTeam'])



def get_team_image(team_id, team_name):
    #   Check for team image in database
    team_logo = TeamLogo.objects.filter(team_id=team_id).first()

    if team_logo:
        return team_logo.logo_url

    # Run function and save logo to database
    else:

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
            logo_url = logo_tag['src']

            # save team logo to database
            instance = TeamLogo(team_id=team_id, team_name=team_name, logo_url=logo_url)
            instance.save()
            return logo_url

    return None


results = get_scores()

break_down = results[2]['homeTeam']['periods']

""""
for quarter in break_down:
    print(fPeriod: {quarter['period']} \n Period Type: {quarter['periodType']}\n Score: {quarter['score']})
"""
