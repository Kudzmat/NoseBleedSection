from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import leaguestandings, playerawards, commonplayerinfo, leagueleaders
from nba_today.models import TeamLogo
from nba_stats.functions import get_player_image


def get_league_leaders():
    stats = ["PTS", "BLK", "REB", "AST", "STL"]
    stat_leaders = {}

    # points per game
    for category in stats:
        leaders = leagueleaders.LeagueLeaders(per_mode48='PerGame', stat_category_abbreviation=category)
        leaders_info = leaders.get_dict()

        # get stat location by index
        leaders_list = leaders_info['resultSet']['headers']
        stat_index = leaders_list.index(category)

        # player name and headshot
        player_name = leaders_info['resultSet']['rowSet'][0][2]
        player_id = leaders_info['resultSet']['rowSet'][0][0]
        player_headshot = get_player_image(player_id, player_name)
        player_image = player_headshot[0]
        team_colour = player_headshot[1]

        # stat
        stat = leaders_info['resultSet']['rowSet'][0][stat_index]

        stat_leaders[category] = [player_name, stat, player_image, team_colour, player_id]

    return stat_leaders


def get_player_bio(player_name):
    bio = {}

    # get player id
    player_name = players.find_players_by_full_name(player_name)
    player_id = player_name[0]['id']

    # get player info
    player_info = commonplayerinfo.CommonPlayerInfo(player_id)
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
    team_id = bio['team_id']

    if status == "Active":
        # get team logo and colour
        team_logo = TeamLogo.objects.filter(team_id=team_id).first()
        if team_logo:
            bio['team_image'] = team_logo.logo_url
            bio['team_colour'] = team_logo.team_colour
    else:
        bio['team_image'] = "None"
        bio['team_colour'] = "#7E354D"

    return bio


def get_accolades(player_name):
    accolades = []
    accolades_history = {}

    # get player info to access player id
    player_info = players.find_players_by_full_name(player_name)
    player_id = player_info[0]['id']

    # get list of accolades
    player_accolades = playerawards.PlayerAwards(player_id)

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
