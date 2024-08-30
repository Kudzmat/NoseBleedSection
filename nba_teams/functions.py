from nba_today.functions import get_team_image
from nba_today.models import TeamLogo
from nba_stats.functions import get_player_image
from nba_api.stats.endpoints import teamdetails, commonteamroster, teaminfocommon, leaguegamefinder


def get_team(team_id):
    team = TeamLogo.objects.filter(team_id=team_id).first()

    if team:
        return team.team_id, team.team_name, team.logo_url, team.team_city, team.team_colour, team.team_full_name, team.team_city


def get_team_history(team_id):
    # this is the info we need
    team_specifics = ['HEADCOACH', 'ARENA']
    current_history = {}
    team_championships = {}

    # get dictionary of information
    team_details = teamdetails.TeamDetails(team_id=team_id)
    team_details = team_details.get_dict()

    # team championships
    chips = team_details['resultSets'][3]['rowSet']

    # team coach and arena
    basic_info = team_details['resultSets'][0]['headers']
    team_info = team_details['resultSets'][0]['rowSet'][0]
    for item in team_specifics:
        info = basic_info.index(item)
        current_history[item] = team_info[info]

    for year, team in chips:
        team_championships[year] = [team]

    return current_history, team_championships


def retired_players(team_id):
    retired_info = ['PLAYERID', 'PLAYER', 'POSITION', 'JERSEY', 'SEASONSWITHTEAM']
    retired_guys = []  # will contain lists of players and their information

    team_details = teamdetails.TeamDetails(team_id=team_id)
    team_details = team_details.get_dict()
    retired_headings = team_details['resultSets'][6]['headers']
    retired = team_details['resultSets'][7]['rowSet']
    count = 0

    while count < len(retired):
        player_info = []
        for item in retired_info:
            info = retired_headings.index(item)
            player_info.append(retired[count][info])

        retired_guys.append(player_info)
        count += 1

    return retired_guys


def get_team_roster(team_id):
    final_roster = []  # will contain lists of players and their information
    player_info = ['PLAYER_ID', 'PLAYER', 'NUM', 'POSITION', 'HEIGHT', 'WEIGHT', 'AGE', 'EXP']  # also need player id
    team_details = commonteamroster.CommonTeamRoster(team_id=team_id)
    team_roster = team_details.get_dict()
    roster_headings = team_roster['resultSets'][0]['headers']
    lakers_roster = team_roster['resultSets'][0]['rowSet']
    count = 0

    while count < len(lakers_roster):
        player_details = []
        for item in player_info:
            # PLAYERID
            # PLAYER - --> Jalen Hood-Schifino
            # NUM - --> 0
            # POSITION - --> G
            # HEIGHT - --> 6-5
            # WEIGHT - --> 215
            # AGE - --> 21.0
            # EXP ---> R
            info = roster_headings.index(item)
            player_details.append(lakers_roster[count][info])

        # append player headshot and team colour
        # get player id
        player_id = player_details[0]

        # get player name
        player_name = player_details[1]

        # call function and append
        player_specs = get_player_image(player_id, player_name)
        player_head_shot = player_specs[0]
        player_details.append(player_head_shot)
        team_colour = player_specs[1]
        player_details.append(team_colour)

        # append player details to final roster
        final_roster.append(player_details)
        count += 1

    return final_roster


def get_team_rankings(team_id):
    team_ranks = {}
    team_record = ['TEAM_CONFERENCE', 'TEAM_DIVISION', 'W', 'L']
    team_rankings = ['PTS_RANK', 'PTS_PG', 'REB_RANK', 'REB_PG', 'AST_RANK', 'AST_PG', 'OPP_PTS_RANK', 'OPP_PTS_PG']
    rankings = teaminfocommon.TeamInfoCommon(team_id=team_id)
    rankings = rankings.get_dict()
    record_headings = rankings['resultSets'][0]['headers']
    record = rankings['resultSets'][0]['rowSet'][0]

    # team conferences & record
    for item in team_record:
        info = record_headings.index(item)
        team_ranks[item] = record[info]

    # team league rankings
    team_rankings_info = rankings['resultSets'][1]['rowSet'][0]
    team_rank_headings = rankings['resultSets'][1]['headers']
    for item in team_rankings:
        info = team_rank_headings.index(item)
        team_ranks[item] = team_rankings_info[info]

    return team_ranks

