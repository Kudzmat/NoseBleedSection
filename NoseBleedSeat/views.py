from django.shortcuts import render, redirect
from nba_stats.forms import PlayerSearchForm
from nba_api.stats.static import players
from .functions import *
from nba_stats.functions import *


def home(request):
    # get player profiles
    player1 = "Kobe Bryant"
    player2 = 'Michael Jordan'

    # get headshots
    player1_info = players.find_players_by_full_name(player1)
    player1_id = player1_info[0]['id']
    player1_image = get_player_image(player1_id, player1)

    player2_info = players.find_players_by_full_name(player2)
    player2_id = player2_info[0]['id']
    player2_image = get_player_image(player2_id, player2)

    # Get player career stats
    player1_stats = player_career_numbers(player1_id)
    player2_stats = player_career_numbers(player2_id)

    # getting player1 per game averages
    for season_data in player1_stats:

        # points per game
        if season_data['GP'] > 0:
            season_data['PPG'] = round(season_data['PTS'] / season_data['GP'], 2)
        else:
            season_data['PPG'] = 0  # To avoid division by zero in case GP is 0

        # assists per game
        if season_data['GP'] > 0:
            season_data['APG'] = round(season_data['AST'] / season_data['GP'], 1)
        else:
            season_data['APG'] = 0

        # blocks per game
        if season_data['GP'] > 0:
            season_data['BLKPG'] = round(season_data['BLK'] / season_data['GP'], 1)
        else:
            season_data['BLKPG'] = 0

        # rebounds per game
        if season_data['GP'] > 0:
            season_data['RPG'] = round(season_data['REB'] / season_data['GP'], 1)
        else:
            season_data['RPG'] = 0

        # steals per game
        if season_data['GP'] > 0:
            season_data['STLPG'] = round(season_data['STL'] / season_data['GP'], 1)
        else:
            season_data['STLPG'] = 0

        # Certain players (specifically from before 1980) don't have a 3pt %
        if season_data['FG3_PCT'] is None:
            season_data['FG3_PCT'] = 0

            # getting player2 per game averages
    for season_data in player2_stats:

        # points per game
        if season_data['GP'] > 0:
            season_data['PPG'] = round(season_data['PTS'] / season_data['GP'], 2)
        else:
            season_data['PPG'] = 0  # To avoid division by zero in case GP is 0

        # assists per game
        if season_data['GP'] > 0:
            season_data['APG'] = round(season_data['AST'] / season_data['GP'], 1)
        else:
            season_data['APG'] = 0

        # blocks per game
        if season_data['GP'] > 0:
            season_data['BLKPG'] = round(season_data['BLK'] / season_data['GP'], 1)
        else:
            season_data['BLKPG'] = 0

        # rebounds per game
        if season_data['GP'] > 0:
            season_data['RPG'] = round(season_data['REB'] / season_data['GP'], 1)
        else:
            season_data['RPG'] = 0

        # steals per game
        if season_data['GP'] > 0:
            season_data['STLPG'] = round(season_data['STL'] / season_data['GP'], 1)
        else:
            season_data['STLPG'] = 0

        # Certain players (specifically from before 1980) don't have a 3pt %
        if season_data['FG3_PCT'] is None:
            season_data['FG3_PCT'] = 0

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
        'player2': player2,
    }
    return render(request, "index.html", context=context)
