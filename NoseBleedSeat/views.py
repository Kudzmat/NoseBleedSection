from django.shortcuts import render, redirect
from nba_stats.forms import PlayerSearchForm, TeamSearchForm
from nba_api.stats.static import players
from nba_stats.models import *
from .functions import *
from nba_stats.functions import *
from nba_teams.functions import get_team
from .forms import PlayerOneForm, PlayerTwoForm
from nba_teams.models import *


def home(request):
    # Delete session data
    request.session.pop('player_page_info', None)
    request.session.pop('player_info', None)



    player_compare_info = []
    player1 = request.session.get('player1', "Kobe Bryant")
    player2 = request.session.get('player2', 'Reggie Miller')

    try:
        # Fetch player data
        player1_headshot, player1_bio, player1_id = fetch_player_data(player1)
        player2_headshot, player2_bio, player2_id = fetch_player_data(player2)

        if not player1_headshot or not player2_headshot:
            raise ValueError("Player not found")

    except ValueError as e:
        # Instead of redirecting, render your custom error page
        context = {
            'message': 'Player not found. Please check the spelling and try again.'
        }
        request.session.pop('player2', None)
        request.session.pop('player1', None)
        return render(request, 'error.html', context)

    # Prepare player images and awards
    player1_image = [player1_headshot.player_image_url, player1_headshot.background_colour]
    player2_image = [player2_headshot.player_image_url, player2_headshot.background_colour]
    player1_awards = get_player_awards(player1, player1_headshot.player_id)
    player2_awards = get_player_awards(player2, player2_headshot.player_id)

    eastern_teams = EasternConferenceTeams.objects.all()
    western_teams = WesternConferenceTeams.objects.all()

    # Add player 1 and player 2 data to session for comparison
    player_compare_info.extend([player1_id, player2_id, player1, player2])
    request.session['player_compare_info'] = player_compare_info

    player_form = PlayerSearchForm()
    player1_form = PlayerOneForm()
    player2_form = PlayerTwoForm()

    if request.method == 'POST':
        try:
            # Handle the main search form
            player_form = PlayerSearchForm(request.POST)
            if player_form.is_valid():
                search_term = player_form.cleaned_data['player_name'].title()

                # Search for the team by name
                team_id = search_team_by_name(search_term, eastern_teams, western_teams)
                if team_id:
                    return redirect('nba_teams:team_page', team_id=team_id)

                # Search for the player data
                player_headshot, player_bio, player_id = fetch_player_data(search_term)
                if not player_headshot:
                    raise ValueError("Player not found")

                player_full_name = player_headshot.player_name
                player_headshot = [player_headshot.player_image_url, player_headshot.background_colour]
                request.session['player_info'] = [player_headshot, player_bio]

                return redirect('nba_stats:player_details', player_id=player_id, player_full_name=player_full_name)

            # Handle player1 and player2 search forms
            player1_form = PlayerOneForm(request.POST)
            player2_form = PlayerTwoForm(request.POST)
            if player1_form.is_valid():
                request.session['player1'] = player1_form.cleaned_data['player1_name'].title()
                return redirect('home')
            if player2_form.is_valid():
                request.session['player2'] = player2_form.cleaned_data['player2_name'].title()
                return redirect('home')

        except ValueError as e:
            context = {
                'message': "Player not found. Please check the spelling and try again."
            }
            return render(request, 'error.html', context)

    context = {
        'player_form': player_form,
        'player1_id': player1_id,
        'player2_id': player2_id,
        'player1_form': player1_form,
        'player2_form': player2_form,
        'player1_awards': player1_awards,
        'player2_awards': player2_awards,
        'player1_image': player1_image,
        'player2_image': player2_image,
        'player1': player1,
        'player2': player2,
        'player1_bio': player1_bio,
        'player2_bio': player2_bio,
        'league_leaders': get_league_leaders(),
    }

    return render(request, "index.html", context=context)

