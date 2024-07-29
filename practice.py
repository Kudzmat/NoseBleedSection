from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import leaguestandings, playerawards
import pprint

bron = players.find_players_by_full_name("Austin Reaves")
bron_id = bron[0]['id']

bron_stats = playerawards.PlayerAwards(bron_id)

count = 0
AWARDS = ["All-Defensive Team",
          "All-NBA", "All-Rookie Team",
          "NBA All-Star Most Valuable Player",
          "NBA Finals Most Valuable Player",
          "NBA Most Valuable Player",
          "NBA Player of the Month",
          "NBA Player of the Week",
          "NBA Rookie of the Month",
          "Olympic Bronze Medal",
          "Olympic Gold Medal",
          "Olympic Silver Medal",
          "NBA In-Season Tournament Most Valuable Player",
          "NBA In-Season Tournament All-Tournament",
          "NBA All-Star",
          "NBA Champion"
          ]
accolades = []
accolades_data = {}
bron_awards = bron_stats.get_data_frames()[0]
for info in bron_awards['DESCRIPTION']:
    accolades.append(info)

accolades.sort()
count = 1
for num,award in enumerate(accolades):
    if num + 1 < len(accolades) and award == accolades[num + 1]:
        count += 1
    else:
        accolades_data[award] = count
        count = 1

print(accolades_data)
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
