from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import leaguestandings, playerawards, commonplayerinfo, leagueleaders
import pprint

# get player id
player_name = "Stephen Curry"
player_name = players.find_players_by_full_name(player_name)
player_id = player_name[0]['id']

team_ids = [
    "1610612737",
    "1610612738",
    "1610612751",
    "1610612766",
    "1610612741",
    "1610612739",
    "1610612742",
    "1610612743",
    "1610612765",
    "1610612744",
    "1610612745",
    "1610612754",
    "1610612746",
    "1610612747",
    "1610612763",
    "1610612748",
    "1610612749",
    "1610612750",
    "1610612740",
    "1610612752",
    "1610612760",
    "1610612753",
    "1610612755",
    "1610612756",
    "1610612757",
    "1610612758",
    "1610612759",
    "1610612761",
    "1610612762",
    "1610612764"
]

standings_info = leaguestandings.LeagueStandings()
standings = standings_info.get_dict()
team_standings = standings['resultSets'][0]['rowSet']
print(team_standings[5])
# get player info
player_id2 = 1641705
player_info = commonplayerinfo.CommonPlayerInfo(player_id2)
player_bio = player_info.get_dict()
#print(player_bio)





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

team_colours2 = {1610612737: '#e03a3e', 1610612738: '#007A33', 1610612751: '#000000', 1610612766: '#00788c',
                 1610612749: '#00471b', 1610612754: '#002d62', 1610612748: '#98002e', 1610612755: '#006bb6',
                 1610612752: '#f58426', 1610612765: '#c8102e', 1610612757: '#e03a3e', 1610612759: '#c4ced4',
                 1610612760: '#007ac1', 1610612758: '#5a2d81', 1610612761: '#ce1141', 1610612762: '#00a9e0',
                 1610612740: '#0c2340', 1610612742: '#00538c', 1610612747: '#f9a01b', 1610612743: '#1d428a',
                 1610612744: '#ffc72c', 1610612745: '#ce1141', 1610612746: '#1d428a', 1610612763: '#5d76a9',
                 1610612750: '#236192', 1610612753: '#0077c0', 1610612756: '#e56020', 1610612764: '#002b5c',
                 1610612739: '#860038', 1610612741: '#ce1141'}

# mj = players.find_players_by_full_name("Michael Jordan")
# print(mj)


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
