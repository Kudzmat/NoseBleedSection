from django.core.management.base import BaseCommand
from nba_teams.models import EasternConferenceTeams, WesternConferenceTeams


class Command(BaseCommand):
    help = 'Inserts NBA teams into the database'

    help = 'Inserts NBA teams into the database'

    def handle(self, *args, **kwargs):
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
                'team_name': 'Spurs',
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

        # Insert Eastern Conference Teams
        for team in eastern_conference_teams:
            EasternConferenceTeams.objects.update_or_create(
                team_id=team['team_id'],
                team_full_name=team['team_full_name'],
                team_name=team['team_name'],
                team_abbreviated=team['team_abbreviated'],
                team_city=team['team_city'],
                team_logo_url=team['team_logo_url'],
                team_colour=team['team_colour']
            )

        # Insert Western Conference Teams
        for team in western_conference_teams:
            WesternConferenceTeams.objects.update_or_create(
                team_id=team['team_id'],
                team_full_name=team['team_full_name'],
                team_name=team['team_name'],
                team_abbreviated=team['team_abbreviated'],
                team_city=team['team_city'],
                team_logo_url=team['team_logo_url'],
                team_colour=team['team_colour']
            )

        self.stdout.write(self.style.SUCCESS('Successfully inserted NBA teams'))
