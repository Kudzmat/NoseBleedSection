from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import leaguestandings, playerawards


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
