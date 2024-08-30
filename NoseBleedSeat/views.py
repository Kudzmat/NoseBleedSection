from django.shortcuts import render, redirect
from nba_stats.forms import PlayerSearchForm, TeamSearchForm
from nba_api.stats.static import players
from .functions import *
from nba_stats.functions import *
from nba_teams.functions import get_team
from .forms import PlayerOneForm, PlayerTwoForm
from nba_today.models import TeamLogo


def home(request):
    player_compare_info = []
    player1 = request.session.get('player1', None)
    player2 = request.session.get('player2', None)

    # Default player values
    if player1 is None:
        player1 = "Dwyane Wade"
    if player2 is None:
        player2 = 'James Harden'

    league_teams = TeamLogo.objects.all()
    team_id = None

    # Get headshots and bios for player comparison
    player1_info = players.find_players_by_full_name(player1)
    player1_id = player1_info[0]['id']
    player1_image = get_player_image(player1_id, player1)
    player1_bio = get_player_bio(player1)

    player2_info = players.find_players_by_full_name(player2)
    player2_id = player2_info[0]['id']
    player2_image = get_player_image(player2_id, player2)
    player2_bio = get_player_bio(player2)

    # Store comparison data in session
    player_compare_info.extend([player1_id, player2_id, player1, player2])
    request.session['player_compare_info'] = player_compare_info

    # Get league leaders
    league_leaders = get_league_leaders()

    # Get player awards
    player1_awards = get_accolades(player1)
    player2_awards = get_accolades(player2)

    # Initialize forms
    player_form = PlayerSearchForm()
    player1_form = PlayerOneForm()
    player2_form = PlayerTwoForm()

    if request.method == 'POST':
        player_form = PlayerSearchForm(request.POST)
        player1_form = PlayerOneForm(request.POST)
        player2_form = PlayerTwoForm(request.POST)

        if player_form.is_valid():
            # Get search term
            search_term = player_form.cleaned_data['player_name']
            search_term = search_term.title()  # NBA API is case sensitive

            # Check if search term matches a team
            for team in league_teams:
                if search_term in [team.team_name, team.team_full_name, team.team_city]:
                    team_id = int(team.team_id)
                    break

            if team_id:
                # Redirect to team page if a team was found
                return redirect('nba_teams:team_page', team_id=team_id)
            else:
                # Check if search term matches a player
                player_info = players.find_players_by_full_name(search_term)
                if player_info:
                    player_id = player_info[0]['id']
                    player_full_name = player_info[0]['full_name']
                    return redirect('nba_stats:player_details', player_id=player_id, player_full_name=player_full_name)

        if player1_form.is_valid():
            player1 = player1_form.cleaned_data['player1_name'].title()
            request.session['player1'] = player1
            return redirect('home')

        if player2_form.is_valid():
            player2 = player2_form.cleaned_data['player2_name'].title()
            request.session['player2'] = player2
            return redirect('home')

    context = {
        'player_form': player_form,
        'player1_form': player1_form,
        'player2_form': player2_form,
        'player1_awards': player1_awards,
        'player2_awards': player2_awards,
        'player1_image': player1_image,
        'player2_image': player2_image,
        'player1': player1,
        'player1_id': player1_id,
        'player2_id': player2_id,
        'player2': player2,
        'player1_bio': player1_bio,
        'player2_bio': player2_bio,
        'league_leaders': league_leaders
    }
    return render(request, "index.html", context=context)

