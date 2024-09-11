from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import teamdetails, commonteamroster, teaminfocommon, leaguegamefinder,commonplayerinfo
import pprint
from nba_stats.functions import *

# get player id
player_name = "lebron james"
player_name = players.find_players_by_full_name(player_name)
print(player_name)
player_id = player_name[0]['id']
player_name = player_name[0]['full_name']
print(player_name)

wemby = 1641705
player_stats = playercareerstats.PlayerCareerStats(player_id=wemby)
career_dict = player_stats.get_normalized_dict()

print(career_dict)


STAT_OPTIONS2 = (
    ('--- Stats Totals By Year ---', '--- Stats Totals By Year  ---'),
    ('SeasonTotalsRegularSeason', 'Reg. Season'),
    ('SeasonTotalsPostSeason', 'Post Season'),
    ('SeasonRankingsRegularSeason', 'Reg. Season Rankings'),
    ('SeasonRankingsPostSeason', 'Post Season Rankings'),

)




# info = players.find_players_by_full_name("lakers")
# if len(info) == 0:
#     info = teamdetails.TeamDetails(team_id=1610612747)
#     print(info.get_dict())
# elif len(info) > 0:
#     print(info)
# else:
#     print("Not sure what to do")


# search for team using database and not api
# team = "Los Angels Lakers"
# league_teams = teams.get_teams()
# print(league_teams)

def get_team_games():
    lake_show = 1610612747
    # Query for games where the Celtics were playing
    game_finder = leaguegamefinder.LeagueGameFinder()
    # The first DataFrame of those returned is what we want.
    games = game_finder.get_dict()

    print(games)


def get_team_history():
    # this is the info we need at index 0
    info_0 = ['HEADCOACH', 'ARENA']

    lake_show = 1610612747
    team_details = teamdetails.TeamDetails(team_id=lake_show)
    team_details = team_details.get_dict()
    chips = team_details['resultSets'][3]['rowSet']
    print(len(chips))
    basic_info = team_details['resultSets'][0]['headers']
    team_info = team_details['resultSets'][0]['rowSet'][0]
    for item in info_0:
        info = basic_info.index(item)
        print(f"{item} -> {team_info[info]}")

    for year, team in chips:
        print(f"""
        Lakers Chips:
        Year   |   Opponent
        {year}      {team}""")


def team_hof():
    retired_guys = []
    retired_info = ['PLAYERID', 'PLAYER', 'POSITION', 'JERSEY', 'SEASONSWITHTEAM']
    lake_show = 1610612747
    team_details = teamdetails.TeamDetails(team_id=lake_show)
    team_details = team_details.get_dict()
    retired_headings = team_details['resultSets'][6]['headers']
    retired = team_details['resultSets'][7]['rowSet']
    count = 0

    while count < len(retired):
        player_info = []
        for item in retired_info:
            info = retired_headings.index(item)
            player_info.append(retired[count][info])

            # print(f"{item} --> {retired[count][info]}")
        # print("------------")
        retired_guys.append(player_info)
        count += 1

    print(retired_guys)


def get_team_roster():
    player_info = ['PLAYER', 'NUM', 'POSITION', 'HEIGHT', 'WEIGHT', 'AGE', 'EXP']  # also need player id
    lake_show = 1610612747
    lakers = commonteamroster.CommonTeamRoster(team_id=lake_show)
    lakers_roster = lakers.get_dict()
    basic_roster = lakers_roster['resultSets'][0]['headers']
    lakers_roster = lakers_roster['resultSets'][0]['rowSet']
    count = 0

    print("Lakers Roster:")
    while count < len(lakers_roster):
        for item in player_info:
            info = basic_roster.index(item)
            print(f"{item} ---> {lakers_roster[count][info]}")
        print("-------------------------------")
        count += 1


def get_team_rankings():
    team_record = ['TEAM_CONFERENCE', 'TEAM_DIVISION', 'W', 'L']
    team_rankings = ['PTS_RANK', 'PTS_PG', 'REB_RANK', 'REB_PG', 'AST_RANK', 'AST_PG', 'OPP_PTS_RANK', 'OPP_PTS_PG']
    lake_show = 1610612747
    rankings = teaminfocommon.TeamInfoCommon(team_id=lake_show)
    rankings = rankings.get_dict()
    record_headings = rankings['resultSets'][0]['headers']
    record = rankings['resultSets'][0]['rowSet'][0]
    for item in team_record:
        info = record_headings.index(item)
        print(f"{item} ---> {record[info]}")

    team_rankings_info = rankings['resultSets'][1]['rowSet'][0]
    team_rank_headings = rankings['resultSets'][1]['headers']
    for item in team_rankings:
        info = team_rank_headings.index(item)
        print(f"{item} ---> {team_rankings_info[info]}")


#team_hof()
# team history
# team_leaders = teamhistoricalleaders.TeamHistoricalLeaders(team_id=lake_show)
# team_leaders = team_leaders.get_dict()

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

clubs2 = {
    1610612737: 'Hawks',
    1610612738: 'Celtics',
    1610612751: 'Nets',
    1610612766: 'Hornets',
    1610612749: 'Bucks',
    1610612754: 'Pacers',
    1610612748: 'Heat',
    1610612755: 'Sixers',
    1610612752: 'Knicks',
    1610612765: 'Pistons',
    1610612757: 'Blazers',
    1610612759: 'Spurs',
    1610612760: 'Thunder',
    1610612758: 'Kings',
    1610612761: 'Raptors',
    1610612762: 'Jazz',
    1610612740: 'Pelicans',
    1610612742: 'Mavericks',
    1610612747: 'Lakers',
    1610612743: 'Nuggets',
    1610612744: 'Warriors',
    1610612745: 'Rockets',
    1610612746: 'Clippers',
    1610612763: 'Grizzlies',
    1610612750: 'Timberwolves',
    1610612753: 'Magic',
    1610612756: 'Suns',
    1610612764: 'Wizards',
    1610612739: 'Cavaliers',
    1610612741: 'Bulls',

}

team_logos = 'Celtics', 'https://cdn.nba.com/logos/nba/1610612738/global/L/logo.svg'

clubs = {1610612737: 'Hawks', 1610612738: 'Celtics', 1610612751: 'Nets', 1610612766: 'Hornets', 1610612749: 'Bucks',
         1610612754: 'Pacers', 1610612748: 'Heat', 1610612755: 'Sixers', 1610612752: 'Knicks', 1610612765: 'Pistons',
         1610612757: 'Blazers', 1610612759: 'Spurs', 1610612760: 'Thunder', 1610612758: 'Kings', 1610612761: 'Raptors',
         1610612762: 'Jazz', 1610612740: 'Pelicans', 1610612742: 'Mavericks', 1610612747: 'Lakers',
         1610612743: 'Nuggets', 1610612744: 'Warriors', 1610612745: 'Rockets', 1610612746: 'Clippers',
         1610612763: 'Grizzlies', 1610612750: 'Timberwolves', 1610612753: 'Magic', 1610612756: 'Suns',
         1610612764: 'Wizards', 1610612739: 'Cavaliers', 1610612741: 'Bulls'}

cities = {1610612737: 'Atlanta', 1610612738: 'Boston', 1610612751: 'Brooklyn', 1610612766: 'Charlotte',
          1610612749: 'Milwaukee', 1610612754: 'Indiana', 1610612748: 'Miami', 1610612755: 'Philadelphia',
          1610612752: 'New York', 1610612765: 'Detroit', 1610612757: 'Portland', 1610612759: 'San Antonio',
          1610612760: 'Oklahoma City', 1610612758: 'Sacramento', 1610612761: 'Toronto', 1610612762: 'Utah',
          1610612740: 'New Orleans', 1610612742: 'Dallas', 1610612747: 'Los Angeles', 1610612743: 'Denver',
          1610612744: 'Golden State', 1610612745: 'Houston', 1610612746: 'Los Angeles', 1610612763: 'Memphis',
          1610612750: 'Minnesota', 1610612753: 'Orlando', 1610612756: 'Phoenix', 1610612764: 'Washington',
          1610612739: 'Cleveland', 1610612741: 'Chicago'}

team_colours2 = {1610612737: '#e03a3e', 1610612738: '#007A33', 1610612751: '#000000', 1610612766: '#00788c',
                 1610612749: '#00471b', 1610612754: '#002d62', 1610612748: '#98002e', 1610612755: '#006bb6',
                 1610612752: '#f58426', 1610612765: '#c8102e', 1610612757: '#e03a3e', 1610612759: '#c4ced4',
                 1610612760: '#007ac1', 1610612758: '#5a2d81', 1610612761: '#ce1141', 1610612762: '#00a9e0',
                 1610612740: '#0c2340', 1610612742: '#00538c', 1610612747: '#f9a01b', 1610612743: '#1d428a',
                 1610612744: '#ffc72c', 1610612745: '#ce1141', 1610612746: '#1d428a', 1610612763: '#5d76a9',
                 1610612750: '#236192', 1610612753: '#0077c0', 1610612756: '#e56020', 1610612764: '#002b5c',
                 1610612739: '#860038', 1610612741: '#ce1141'}

# Data for all NBA Eastern Conference teams
eastern_conference_teams = [
    {
        'team_id': 1610612738,
        'team_full_name': 'Boston Celtics',
        'team_name': 'Celtics',
        'team_abbreviated': 'BOS',
        'team_city': 'Boston',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612738/global/L/logo.svg',
        'team_colour': '#007A33'
    },
    {
        'team_id': 1610612741,
        'team_full_name': 'Chicago Bulls',
        'team_name': 'Bulls',
        'team_abbreviated': 'CHI',
        'team_city': 'Chicago',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612741/global/L/logo.svg',
        'team_colour': '#CE1141'
    },
    {
        'team_id': 1610612739,
        'team_full_name': 'Cleveland Cavaliers',
        'team_name': 'Cavaliers',
        'team_abbreviated': 'CLE',
        'team_city': 'Cleveland',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612739/global/L/logo.svg',
        'team_colour': '#860038'
    },
    {
        'team_id': 1610612765,
        'team_full_name': 'Detroit Pistons',
        'team_name': 'Pistons',
        'team_abbreviated': 'DET',
        'team_city': 'Detroit',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612765/global/L/logo.svg',
        'team_colour': '#C8102E'
    },
    {
        'team_id': 1610612754,
        'team_full_name': 'Indiana Pacers',
        'team_name': 'Pacers',
        'team_abbreviated': 'IND',
        'team_city': 'Indiana',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612754/global/L/logo.svg',
        'team_colour': '#002D62'
    },
    {
        'team_id': 1610612748,
        'team_full_name': 'Miami Heat',
        'team_name': 'Heat',
        'team_abbreviated': 'MIA',
        'team_city': 'Miami',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612748/global/L/logo.svg',
        'team_colour': '#98002E'
    },
    {
        'team_id': 1610612749,
        'team_full_name': 'Milwaukee Bucks',
        'team_name': 'Bucks',
        'team_abbreviated': 'MIL',
        'team_city': 'Milwaukee',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612749/global/L/logo.svg',
        'team_colour': '#00471B'
    },
    {
        'team_id': 1610612752,
        'team_full_name': 'New York Knicks',
        'team_name': 'Knicks',
        'team_abbreviated': 'NYK',
        'team_city': 'New York',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612752/global/L/logo.svg',
        'team_colour': '#F58426'
    },
    {
        'team_id': 1610612753,
        'team_full_name': 'Orlando Magic',
        'team_name': 'Magic',
        'team_abbreviated': 'ORL',
        'team_city': 'Orlando',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612753/global/L/logo.svg',
        'team_colour': '#0077C0'
    },
    {
        'team_id': 1610612755,
        'team_full_name': 'Philadelphia 76ers',
        'team_name': 'Sixers',
        'team_abbreviated': 'PHI',
        'team_city': 'Philadelphia',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612755/global/L/logo.svg',
        'team_colour': '#006BB6'
    },
    {
        'team_id': 1610612751,
        'team_full_name': 'Brooklyn Nets',
        'team_name': 'Nets',
        'team_abbreviated': 'BKN',
        'team_city': 'Brooklyn',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612751/global/L/logo.svg',
        'team_colour': '#000000'
    },
    {
        'team_id': 1610612761,
        'team_full_name': 'Toronto Raptors',
        'team_name': 'Raptors',
        'team_abbreviated': 'TOR',
        'team_city': 'Toronto',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612761/global/L/logo.svg',
        'team_colour': '#CE1141'
    },
    {
        'team_id': 1610612764,
        'team_full_name': 'Washington Wizards',
        'team_name': 'Wizards',
        'team_abbreviated': 'WAS',
        'team_city': 'Washington',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612764/global/L/logo.svg',
        'team_colour': '#002B5C'
    },
    {
        'team_id': 1610612766,
        'team_full_name': 'Charlotte Hornets',
        'team_name': 'Hornets',
        'team_abbreviated': 'CHA',
        'team_city': 'Charlotte',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612766/global/L/logo.svg',
        'team_colour': '#00788C'
    },
    {
        'team_id': 1610612737,
        'team_full_name': 'Atlanta Hawks',
        'team_name': 'Hawks',
        'team_abbreviated': 'ATL',
        'team_city': 'Atlanta',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612737/global/L/logo.svg',
        'team_colour': '#e03a3e'
    },
]

# Data for all NBA Western Conference teams
western_conference_teams = [
    {
        "team_id": 1610612742,
        "team_full_name": "Dallas Mavericks",
        "team_name": "Mavericks",
        "team_abbreviated": "DAL",
        "team_city": "Dallas",
        "team_logo_url": "https://cdn.nba.com/logos/nba/1610612742/global/L/logo.svg",
        "team_colour": "#00538c"
    },
    {
        "team_id": 1610612743,
        "team_full_name": "Denver Nuggets",
        "team_name": "Nuggets",
        "team_abbreviated": "DEN",
        "team_city": "Denver",
        "team_logo_url": "https://cdn.nba.com/logos/nba/1610612743/global/L/logo.svg",
        "team_colour": "#1d428a"
    },
    {
        "team_id": 1610612744,
        "team_full_name": "Golden State Warriors",
        "team_name": "Warriors",
        "team_abbreviated": "GSW",
        "team_city": "Golden State",
        "team_logo_url": "https://cdn.nba.com/logos/nba/1610612744/global/L/logo.svg",
        "team_colour": "#1D428A"
    },
    {
        "team_id": 1610612745,
        "team_full_name": "Houston Rockets",
        "team_name": "Rockets",
        "team_abbreviated": "HOU",
        "team_city": "Houston",
        "team_logo_url": "https://cdn.nba.com/logos/nba/1610612745/global/L/logo.svg",
        "team_colour": "#ce1141"
    },
    {
        "team_id": 1610612746,
        "team_full_name": "LA Clippers",
        "team_name": "Clippers",
        "team_abbreviated": "LAC",
        "team_city": "Los Angeles",
        "team_logo_url": "https://cdn.nba.com/logos/nba/1610612746/global/L/logo.svg",
        "team_colour": "#1d428a"
    },
    {
        "team_id": 1610612747,
        "team_full_name": "Los Angeles Lakers",
        "team_name": "Lakers",
        "team_abbreviated": "LAL",
        "team_city": "Los Angeles",
        "team_logo_url": "https://cdn.nba.com/logos/nba/1610612747/global/L/logo.svg",
        "team_colour": "#f9a01b"
    },
    {
        'team_id': 1610612757,
        'team_full_name': 'Portland Trail Blazers',
        'team_name': 'Blazers',
        'team_abbreviated': 'POR',
        'team_city': 'Portland',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612757/global/L/logo.svg',
        'team_colour': '#E03A3E'
    },
    {
        'team_id': 1610612758,
        'team_full_name': 'Sacramento Kings',
        'team_name': 'Kings',
        'team_abbreviated': 'SAC',
        'team_city': 'Sacramento',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612758/global/L/logo.svg',
        'team_colour': '#5A2D81'
    },
    {
        'team_id': 1610612763,
        'team_full_name': 'Memphis Grizzlies',
        'team_name': 'Grizzlies',
        'team_abbreviated': 'MEM',
        'team_city': 'Memphis',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612763/global/L/logo.svg',
        'team_colour': '#5D76A9'
    },
    {
        'team_id': 1610612750,
        'team_full_name': 'Minnesota Timberwolves',
        'team_name': 'Wolves',
        'team_abbreviated': 'MIN',
        'team_city': 'Minneapolis',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612750/global/L/logo.svg',
        'team_colour': '#0C2340'
    },
    {
        'team_id': 1610612760,
        'team_full_name': 'Oklahoma City Thunder',
        'team_name': 'Thunder',
        'team_abbreviated': 'OKC',
        'team_city': 'Oklahoma City',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612760/global/L/logo.svg',
        'team_colour': '#007AC1'
    },
    {
        'team_id': 1610612759,
        'team_full_name': 'San Antonio Spurs',
        'team_abbreviated': 'SAS',
        'team_city': 'San Antonio',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612759/global/L/logo.svg',
        'team_colour': '#C4CED4'
    },
    {
        'team_id': 1610612762,
        'team_full_name': 'Utah Jazz',
        'team_name': 'Jazz',
        'team_abbreviated': 'UTA',
        'team_city': 'Salt Lake City',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612762/global/L/logo.svg',
        'team_colour': '#002B5C'
    },
    {
        'team_id': 1610612756,
        'team_full_name': 'Phoenix Suns',
        'team_name': 'Suns',
        'team_abbreviated': 'PHX',
        'team_city': 'Phoenix',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612756/global/L/logo.svg',
        'team_colour': '#E56020'
    },
    {
        'team_id': 1610612740,
        'team_full_name': 'New Orleans Pelicans',
        'team_name': 'Pelicans',
        'team_abbreviated': 'NOP',
        'team_city': 'New Orleans',
        'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612740/global/L/logo.svg',
        'team_colour': '#0C2340'
    },
]

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


eastern_conference_teams2 = [{'team_id': 1610612738, 'team_full_name': 'Boston Celtics', 'team_name': 'Celtics', 'team_abbreviated': 'BOS', 'team_city': 'Boston', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612738/global/L/logo.svg', 'team_colour': '#007A33'}, {'team_id': 1610612741, 'team_full_name': 'Chicago Bulls', 'team_name': 'Bulls', 'team_abbreviated': 'CHI', 'team_city': 'Chicago', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612741/global/L/logo.svg', 'team_colour': '#CE1141'}, {'team_id': 1610612739, 'team_full_name': 'Cleveland Cavaliers', 'team_name': 'Cavaliers', 'team_abbreviated': 'CLE', 'team_city': 'Cleveland', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612739/global/L/logo.svg', 'team_colour': '#860038'}, {'team_id': 1610612765, 'team_full_name': 'Detroit Pistons', 'team_name': 'Pistons', 'team_abbreviated': 'DET', 'team_city': 'Detroit', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612765/global/L/logo.svg', 'team_colour': '#C8102E'}, {'team_id': 1610612754, 'team_full_name': 'Indiana Pacers', 'team_name': 'Pacers', 'team_abbreviated': 'IND', 'team_city': 'Indiana', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612754/global/L/logo.svg', 'team_colour': '#002D62'}, {'team_id': 1610612748, 'team_full_name': 'Miami Heat', 'team_name': 'Heat', 'team_abbreviated': 'MIA', 'team_city': 'Miami', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612748/global/L/logo.svg', 'team_colour': '#98002E'}, {'team_id': 1610612749, 'team_full_name': 'Milwaukee Bucks', 'team_name': 'Bucks', 'team_abbreviated': 'MIL', 'team_city': 'Milwaukee', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612749/global/L/logo.svg', 'team_colour': '#00471B'}, {'team_id': 1610612752, 'team_full_name': 'New York Knicks', 'team_name': 'Knicks', 'team_abbreviated': 'NYK', 'team_city': 'New York', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612752/global/L/logo.svg', 'team_colour': '#F58426'}, {'team_id': 1610612753, 'team_full_name': 'Orlando Magic', 'team_name': 'Magic', 'team_abbreviated': 'ORL', 'team_city': 'Orlando', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612753/global/L/logo.svg', 'team_colour': '#0077C0'}, {'team_id': 1610612755, 'team_full_name': 'Philadelphia 76ers', 'team_name': 'Sixers', 'team_abbreviated': 'PHI', 'team_city': 'Philadelphia', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612755/global/L/logo.svg', 'team_colour': '#006BB6'}, {'team_id': 1610612751, 'team_full_name': 'Brooklyn Nets', 'team_name': 'Nets', 'team_abbreviated': 'BKN', 'team_city': 'Brooklyn', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612751/global/L/logo.svg', 'team_colour': '#000000'}, {'team_id': 1610612761, 'team_full_name': 'Toronto Raptors', 'team_name': 'Raptors', 'team_abbreviated': 'TOR', 'team_city': 'Toronto', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612761/global/L/logo.svg', 'team_colour': '#CE1141'}, {'team_id': 1610612764, 'team_full_name': 'Washington Wizards', 'team_name': 'Wizards', 'team_abbreviated': 'WAS', 'team_city': 'Washington', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612764/global/L/logo.svg', 'team_colour': '#002B5C'}, {'team_id': 1610612766, 'team_full_name': 'Charlotte Hornets', 'team_name': 'Hornets', 'team_abbreviated': 'CHA', 'team_city': 'Charlotte', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612766/global/L/logo.svg', 'team_colour': '#00788C'}, {'team_id': 1610612737, 'team_full_name': 'Atlanta Hawks', 'team_name': 'Hawks', 'team_abbreviated': 'ATL', 'team_city': 'Atlanta', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612737/global/L/logo.svg', 'team_colour': '#e03a3e'}]

western_conference_teams2 = [{'team_id': 1610612742, 'team_full_name': 'Dallas Mavericks', 'team_name': 'Mavericks', 'team_abbreviated': 'DAL', 'team_city': 'Dallas', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612742/global/L/logo.svg', 'team_colour': '#00538c'}, {'team_id': 1610612743, 'team_full_name': 'Denver Nuggets', 'team_name': 'Nuggets', 'team_abbreviated': 'DEN', 'team_city': 'Denver', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612743/global/L/logo.svg', 'team_colour': '#1d428a'}, {'team_id': 1610612744, 'team_full_name': 'Golden State Warriors', 'team_name': 'Warriors', 'team_abbreviated': 'GSW', 'team_city': 'Golden State', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612744/global/L/logo.svg', 'team_colour': '#1D428A'}, {'team_id': 1610612745, 'team_full_name': 'Houston Rockets', 'team_name': 'Rockets', 'team_abbreviated': 'HOU', 'team_city': 'Houston', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612745/global/L/logo.svg', 'team_colour': '#ce1141'}, {'team_id': 1610612746, 'team_full_name': 'LA Clippers', 'team_name': 'Clippers', 'team_abbreviated': 'LAC', 'team_city': 'Los Angeles', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612746/global/L/logo.svg', 'team_colour': '#1d428a'}, {'team_id': 1610612747, 'team_full_name': 'Los Angeles Lakers', 'team_name': 'Lakers', 'team_abbreviated': 'LAL', 'team_city': 'Los Angeles', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612747/global/L/logo.svg', 'team_colour': '#f9a01b'}, {'team_id': 1610612757, 'team_full_name': 'Portland Trail Blazers', 'team_name': 'Blazers', 'team_abbreviated': 'POR', 'team_city': 'Portland', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612757/global/L/logo.svg', 'team_colour': '#E03A3E'}, {'team_id': 1610612758, 'team_full_name': 'Sacramento Kings', 'team_name': 'Kings', 'team_abbreviated': 'SAC', 'team_city': 'Sacramento', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612758/global/L/logo.svg', 'team_colour': '#5A2D81'}, {'team_id': 1610612763, 'team_full_name': 'Memphis Grizzlies', 'team_name': 'Grizzlies', 'team_abbreviated': 'MEM', 'team_city': 'Memphis', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612763/global/L/logo.svg', 'team_colour': '#5D76A9'}, {'team_id': 1610612750, 'team_full_name': 'Minnesota Timberwolves', 'team_name': 'Wolves', 'team_abbreviated': 'MIN', 'team_city': 'Minneapolis', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612750/global/L/logo.svg', 'team_colour': '#0C2340'}, {'team_id': 1610612760, 'team_full_name': 'Oklahoma City Thunder', 'team_name': 'Thunder', 'team_abbreviated': 'OKC', 'team_city': 'Oklahoma City', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612760/global/L/logo.svg', 'team_colour': '#007AC1'}, {'team_id': 1610612759, 'team_full_name': 'San Antonio Spurs', 'team_name': 'Spurs', 'team_abbreviated': 'SAS', 'team_city': 'San Antonio', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612759/global/L/logo.svg', 'team_colour': '#C4CED4'}, {'team_id': 1610612762, 'team_full_name': 'Utah Jazz', 'team_name': 'Jazz', 'team_abbreviated': 'UTA', 'team_city': 'Salt Lake City', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612762/global/L/logo.svg', 'team_colour': '#002B5C'}, {'team_id': 1610612756, 'team_full_name': 'Phoenix Suns', 'team_name': 'Suns', 'team_abbreviated': 'PHX', 'team_city': 'Phoenix', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612756/global/L/logo.svg', 'team_colour': '#E56020'}, {'team_id': 1610612740, 'team_full_name': 'New Orleans Pelicans', 'team_name': 'Pelicans', 'team_abbreviated': 'NOP', 'team_city': 'New Orleans', 'team_logo_url': 'https://cdn.nba.com/logos/nba/1610612740/global/L/logo.svg', 'team_colour': '#0C2340'}]
