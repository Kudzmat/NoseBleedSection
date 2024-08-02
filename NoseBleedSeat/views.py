from django.shortcuts import render, redirect
from nba_stats.forms import PlayerSearchForm
from nba_api.stats.static import players
from .functions import *
from nba_stats.functions import *


def home(request):
    # get player profiles
    player1 = "Giannis Antetokounmpo"
    player2 = 'Tim Duncan'

    # get headshots
    player1_info = players.find_players_by_full_name(player1)
    player1_id = player1_info[0]['id']
    player1_image = get_player_image(player1_id, player1)
    player1_bio = get_player_bio(player1)

    player2_info = players.find_players_by_full_name(player2)
    player2_id = player2_info[0]['id']
    player2_image = get_player_image(player2_id, player2)
    player2_bio = get_player_bio(player2)

    # Get player career stats
    player1_stats = player_career_numbers(player1_id)
    player2_stats = player_career_numbers(player2_id)

    # get the league leaders in stats
    league_leaders = get_league_leaders()

    player1_awards = get_accolades(player1)
    player2_awards = get_accolades(player2)

    form = PlayerSearchForm()

    if request.method == 'POST':
        form = PlayerSearchForm(request.POST)
        if form.is_valid():
            # Get the player name from the form's cleaned data
            player_name = form.cleaned_data['player_name']
            player_name.title()  # NBA API is case sensitive

            # Use the NBA API to find the player's ID based on the name
            player_info = players.find_players_by_full_name(player_name)

            # Redirect to the search results page
            if player_info:
                player_id = player_info[0]['id']
                player_full_name = player_info[0]['full_name']
                return redirect('nba_stats:player_details', player_id=player_id, player_full_name=player_full_name)
            else:
                return redirect('home')

        else:
            form = PlayerSearchForm()

    context = {
        'form': form,
        'player1_awards': player1_awards,
        'player2_awards': player2_awards,
        'player1_image': player1_image,
        'player2_image': player2_image,
        'player2_stats': player2_stats,
        'player1_stats': player1_stats,
        'player1': player1,
        'player1_id': player1_id,
        'player2_id': player2_id,
        'player2': player2,
        'player1_bio': player1_bio,
        'player2_bio': player2_bio,
        'league_leaders': league_leaders
    }
    return render(request, "index.html", context=context)
