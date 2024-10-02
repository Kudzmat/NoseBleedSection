from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import leaguestandings, playerawards, commonplayerinfo, leagueleaders
import os
import requests
from nba_stats.models import *
from nba_stats.functions import *

# Proxy configuration
SMARTPROXY_URL = os.getenv('SMARTPROXY_URL')
SMARTPROXY_USERNAME = os.getenv('SMARTPROXY_USERNAME')
SMARTPROXY_PASSWORD = os.getenv('SMARTPROXY_PASSWORD')


def fetch_player_data(player_name):
    """Helper function to fetch or create player headshot and bio."""
    player_headshot = PlayerHeadShot.objects.filter(player_name=player_name).first()
    player_bio_data = PlayerBio.objects.filter(player_name=player_name).first()

    if not player_headshot:
        player_info = players.find_players_by_full_name(player_name)

        if not player_info:
            return None, None

        # one more check by player id
        player_id = player_info[0]['id']
        player_headshot = PlayerHeadShot.objects.filter(player_id=player_id).first()
        if player_headshot:
            pass
        else:
            player_name = player_info[0]['full_name']
            player_image = get_player_image(player_id)
            player_url = player_image[0]
            player_team_id = player_image[1]

            player_headshot = PlayerHeadShot.objects.create(
                player_id=player_id,
                player_name=player_name,
                player_image_url=player_url,
                team_id=player_team_id,
                background_colour=None
            )
            player_headshot.save()

    player_id = player_headshot.player_id
    player_name = player_headshot.player_name

    if not player_bio_data:

        # one more check by id
        player_bio_data = PlayerBio.objects.filter(player_id=player_id).first()
        if player_bio_data:
            pass

        else:
            player_bio = get_player_bio(player_id)
            player_bio_data = PlayerBio.objects.create(
                player_id=player_id,
                player_name=player_name,
                school=player_bio.get('education', ''),
                country=player_bio.get('country', ''),
                height=player_bio.get('height', ''),
                weight=player_bio.get('weight', ''),
                year=player_bio.get('year', ''),
                number=player_bio.get('number', ''),
                position=player_bio.get('position', ''),
                team_id=player_bio.get('team_id', ''),
                team_name=player_bio.get('team_name', ''),
                status=player_bio.get('status', ''),
                PTS=player_bio.get('PTS', 0),
                REB=player_bio.get('REB', 0),
                AST=player_bio.get('AST', 0)
            )
            player_bio_data.save()

    player_bio = player_bio_data.__dict__
    player_bio['date'] = player_bio['date'].isoformat()  # to convert date object into string

    return player_headshot, player_bio, player_id


def search_team_by_name(search_term, eastern_teams, western_teams):
    """Helper function to search for a team by name in both conferences."""
    for team in eastern_teams:
        if search_term in [team.team_name, team.team_full_name, team.team_city, team.team_abbreviated]:
            return team.team_id

    for team in western_teams:
        if search_term in [team.team_name, team.team_full_name, team.team_city, team.team_abbreviated]:
            return team.team_id

    return None


def get_player_awards(player_name, player_id):
    awards_data = CareerAwards.objects.filter(player_id=player_id).first()

    if not awards_data:
        player_awards = get_accolades(player_id)
        awards_instance = CareerAwards.objects.create(
            player_id=player_id,
            player_name=player_name,
            accomplishments=player_awards
        )
        awards_instance.save()
    else:
        player_awards = awards_data.accomplishments

    return player_awards


def get_league_leaders():
    # Construct the proxy URL
    proxy_url = f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@gate.smartproxy.com:10001"

    stats = ["PTS", "BLK", "REB", "AST", "STL", "FGM", "FG3M", "FTM", "EFF", "AST_TOV", "STL_TOV"]

    # To map each key with a readable evalue
    stats_map = {
        'PTS': 'Points',
        'BLK': 'Blocks',
        'REB': 'Rebounds',
        'AST': 'Assists',
        'STL': 'Steals',
        'FGM': 'Field Goal Makes',
        'FG3M': '3 Point Field Goal Makes',
        'FTM': 'Free Throw Makes',
        'EFF': 'Individual Player Efficiency',
        'AST_TOV': 'Assists To Turnover Ratio',
        'STL_TOV': 'Steals To Turnover Ratio'

    }
    stat_leaders = {}

    # get league leaders from database
    league_leaders_data = LeagueLeaders.objects.first()

    if league_leaders_data:
        leaders_data = league_leaders_data.leaders
        stat_leaders = leaders_data

    else:

        for category in stats:
            leaders = leagueleaders.LeagueLeaders(stat_category_abbreviation=category, proxy=proxy_url)
            leaders_info = leaders.get_dict()

            # get stat location by index
            leaders_list = leaders_info['resultSet']['headers']
            stat_index = leaders_list.index(category)

            # player name and headshot
            player_name = leaders_info['resultSet']['rowSet'][0][2]
            player_id = leaders_info['resultSet']['rowSet'][0][0]

            # get player headshots
            player_headshot = PlayerHeadShot.objects.filter(player_name=player_name).first()

            if not player_headshot:
                player_headshot = get_player_image(player_id)
                # create and save new instance
                player_headshot_instance = PlayerHeadShot.objects.create(
                    player_id=player_id,
                    player_name=player_name,
                    player_image_url=player_headshot[0],
                    team_id=player_headshot[1],
                    background_colour=None  # This will be dynamically set after saving based on team_id
                )
                player_headshot_instance.save()

                # get player headshots
                player_headshot = PlayerHeadShot.objects.filter(player_id=player_id).first()
                player_image = player_headshot.player_image_url
                team_colour = player_headshot.background_colour

            else:
                player_image = player_headshot.player_image_url
                team_colour = player_headshot.background_colour

            # stat
            stat = leaders_info['resultSet']['rowSet'][0][stat_index]

            category = stats_map[category]

            stat_leaders[category] = [player_name, stat, player_image, team_colour, player_id]

        league_leaders_data = LeagueLeaders.objects.create(
            leaders=stat_leaders
        )
        league_leaders_data.save()

    return stat_leaders


def get_player_bio(player_id):
    # Construct the proxy URL
    proxy_url = f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@gate.smartproxy.com:10001"

    bio = {}

    # get player info
    player_info = commonplayerinfo.CommonPlayerInfo(player_id, proxy=proxy_url)
    player_bio = player_info.get_dict()

    # player stats
    player_stats = player_bio['resultSets'][1]['rowSet'][0]

    # points
    player_pts = player_stats[3]
    bio['PTS'] = player_pts

    # ast
    player_ast = player_stats[4]
    bio['AST'] = player_ast

    # reb
    player_reb = player_stats[5]
    bio['REB'] = player_reb

    # player info
    player_data = player_bio['resultSets'][0]['rowSet'][0]

    # college / high school
    bio['education'] = player_data[8]

    # country
    bio['country'] = player_data[9]

    # height
    bio['height'] = player_data[11]

    # weght
    bio['weight'] = player_data[12]

    # years
    bio['year'] = player_data[13]

    # jersey number
    bio['number'] = player_data[14]

    # position
    bio['position'] = player_data[15]

    # play status
    bio['status'] = player_data[16]
    status = bio['status']

    # team
    bio['team'] = player_data[19]

    # team id
    bio['team_id'] = int(player_data[18])

    return bio


def get_accolades(player_id):
    # Construct the proxy URL
    proxy_url = f"http://{SMARTPROXY_USERNAME}:{SMARTPROXY_PASSWORD}@gate.smartproxy.com:10001"

    accolades = []
    accolades_history = {}

    # get list of accolades
    player_accolades = playerawards.PlayerAwards(player_id, proxy=proxy_url)

    # add award descriptions to accolades empty list
    player_awards = player_accolades.get_data_frames()[0]
    for info in player_awards['DESCRIPTION']:
        accolades.append(info)

    # sort list so that awards are organized alphabetically
    accolades.sort()

    # count how many times an award appears and map it to award
    count = 1
    for num, award in enumerate(accolades):
        if num + 1 < len(accolades) and award == accolades[num + 1]:
            count += 1
        else:
            accolades_history[award] = count
            count = 1

    return accolades_history
