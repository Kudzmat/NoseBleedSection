from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import leaguestandings, playerawards, commonplayerinfo
import pprint

bron = players.find_players_by_full_name("Lebron")
bron_id = bron[0]['id']
print("hi")

print(bron_id)
player_info = commonplayerinfo.CommonPlayerInfo(bron_id)
bron_latest = player_info.get_dict()

player_data = bron_latest['resultSets'][0]['rowSet'][0]
team_data = bron_latest['resultSets'][1]['rowSet'][0]


def get_player_bio(player_name):
    bio = {}

    # get player id
    player_name = players.find_players_by_full_name(player_name)
    player_id = player_name[0]['id']

    # get player info
    player_info = commonplayerinfo.CommonPlayerInfo(player_id)
    player_bio = player_info.get_dict()

    player_data = player_bio['resultSets'][0]['rowSet'][0]
    print(player_data)

    # college / high school
    bio['education'] = player_data[10]

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
        bio['team_image'] = "Yes!!"
        bio['team_colour'] = "YEEEEES"
    else:
        bio['team_image'] = "None"
        bio['team_colour'] = "#7E354D"

    return bio

bio = get_player_bio("Rui Hachimura")

for item in bio.items():
    print(item)




team_colors = {
    1610612737: '#e03a3e',  # Atlanta Hawks
    1610612738: '#007A33',  # Boston Celtics
    1610612751: '#000000',  # Brooklyn Nets
    1610612766: '#00788c',  # Charlotte Hornets
    1610612749: '#00471b',  # Milwaukee Bucks
    1610612754: '#002d62',  # Indiana Pacers
    1610612748: '#98002e',  # Miami Heat
    1610612755: '#006bb6',  # Philadelphia 76ers
    1610612752: '#f58426',  # New York Knicks
    1610612765: '#c8102e',  # Detroit Pistons
    1610612757: '#e03a3e',  # Portland Trail Blazers
    1610612759: '#c4ced4',  # San Antonio Spurs
    1610612760: '#007ac1',  # Oklahoma City Thunder
    1610612758: '#5a2d81',  # Sacramento Kings
    1610612761: '#ce1141',  # Toronto Raptors
    1610612762: '#00a9e0',  # Utah Jazz
    1610612740: '#0c2340',  # New Orleans Pelicans
    1610612742: '#00538c',  # Dallas Mavericks
    1610612747: '#f9a01b',  # Los Angeles Lakers
    1610612743: '#1d428a',  # Denver Nuggets
    1610612744: '#ffc72c',  # Golden State Warriors
    1610612745: '#ce1141',  # Houston Rockets
    1610612746: '#1d428a',  # Los Angeles Clippers
    1610612763: '#5d76a9',  # Memphis Grizzlies
    1610612750: '#236192',  # Minnesota Timberwolves
    1610612753: '#0077c0',  # Orlando Magic
    1610612756: '#e56020',  # Phoenix Suns
    1610612764: '#002b5c',  # Washington Wizards
    1610612739: '#860038',  # Cleveland Cavaliers
    1610612741: '#ce1141',  # Chicago Bulls

}


team_colours2 = {1610612737: '#e03a3e', 1610612738: '#007A33', 1610612751: '#000000', 1610612766: '#00788c', 1610612749: '#00471b', 1610612754: '#002d62', 1610612748: '#98002e', 1610612755: '#006bb6', 1610612752: '#f58426', 1610612765: '#c8102e', 1610612757: '#e03a3e', 1610612759: '#c4ced4', 1610612760: '#007ac1', 1610612758: '#5a2d81', 1610612761: '#ce1141', 1610612762: '#00a9e0', 1610612740: '#0c2340', 1610612742: '#00538c', 1610612747: '#f9a01b', 1610612743: '#1d428a', 1610612744: '#ffc72c', 1610612745: '#ce1141', 1610612746: '#1d428a', 1610612763: '#5d76a9', 1610612750: '#236192', 1610612753: '#0077c0', 1610612756: '#e56020', 1610612764: '#002b5c', 1610612739: '#860038', 1610612741: '#ce1141'}



#mj = players.find_players_by_full_name("Michael Jordan")
#print(mj)



# teams = teams.get_teams()
#
# # Fetch league standings
# standings = leaguestandings.LeagueStandings()
#
# # Get the standings data
# teams_data = standings.get_data_frames()[0]
#
# team_records = {}
# for info in teams_data:
#     team_records = teams_data[['TeamID','TeamCity','TeamName','Record','Conference']]
#
