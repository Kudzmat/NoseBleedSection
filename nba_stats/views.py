from django.shortcuts import render, redirect
from .forms import PlayerSearchForm, StatsDropdownForm, PlayerCompareForm, StatsCompForm
from nba_api.stats.static import players
from .functions import *
from NoseBleedSeat.functions import *


def player_search(request):
    if request.method == 'POST':
        form = PlayerSearchForm(request.POST)
        team_name = ""
        if form.is_valid():
            # Get the player name from the form's cleaned data
            player_name = form.cleaned_data['player_name']
            player_name.title()  # NBA API is case sensitive

            # Use the NBA API to find the player's ID based on the name
            player_info = players.find_players_by_full_name(player_name)

            # Redirect to the search results page
            if len(player_info) > 0:
                player_id = player_info[0]['id']
                player_full_name = player_info[0]['full_name']
                return redirect('nba_stats:player_details', player_id=player_id, player_full_name=player_full_name)

            elif len(player_info) == 0:
                team_name = player_name
                return redirect()

            else:
                # If player not found, show an error message or handle it as needed
                # For simplicity, we'll just redirect back to the search form with an error message
                return redirect('nba_stats:player_search')
    else:
        form = PlayerSearchForm()

    context = {'form': form}

    return render(request, 'nba_stats/player_search.html', context=context)


def player_details(request, player_full_name, player_id):
    # get player headshot
    player_headshot = get_player_image(player_id, player_full_name)

    # Get player career stats
    player_stats = player_career_numbers(player_id)

    # get player bio
    player_bio = get_player_bio(player_full_name)

    # get player awards
    player_awards = get_accolades(player_full_name)

    # stats dropdown form
    form = StatsDropdownForm()

    if request.method == 'POST':
        form = StatsDropdownForm(request.POST)
        if form.is_valid():
            stats_option = form.cleaned_data['option']

            # regular season numbers
            if stats_option == 'Reg. Season':
                return redirect('nba_stats:regular_season', player_id=player_id, player_full_name=player_full_name)

            elif stats_option == 'Post Season':
                return redirect('nba_stats:post_season', player_id=player_id, player_full_name=player_full_name)

            elif stats_option == 'Reg. Season Rankings':
                return redirect('nba_stats:regular_season_rankings', player_id=player_id,
                                player_full_name=player_full_name)

            elif stats_option == 'Post Season Rankings':
                return redirect('nba_stats:post_season_rankings', player_id=player_id,
                                player_full_name=player_full_name)

            else:
                return redirect('home')

    context = {'player_headshot': player_headshot,
               'player_full_name': player_full_name,
               'player_stats': player_stats,
               'player_id': player_id,
               'form': form,
               'player_bio': player_bio,
               'player_awards': player_awards,

               }

    return render(request, 'nba_stats/career_stats.html', context=context)


# regular season totals
def regular_season(request, player_full_name, player_id):
    # Get player headshot
    player_headshot = get_player_image(player_id, player_full_name)

    # Get players yearly numbers
    player_stats = player_regular_season(player_id)

    # get player bio
    player_bio = get_player_bio(player_full_name)

    context = {'player_headshot': player_headshot,
               'player_full_name': player_full_name,
               'player_stats': player_stats,
               'player_id': player_id,
               'player_bio': player_bio,
               }

    return render(request, 'nba_stats/regular_season.html', context=context)


# post season totals
def post_season(request, player_full_name, player_id):
    # Get player headshot
    player_headshot = get_player_image(player_id, player_full_name)

    # Get players yearly numbers
    player_stats = player_post_season(player_id)

    # get player bio
    player_bio = get_player_bio(player_full_name)

    context = {'player_headshot': player_headshot,
               'player_full_name': player_full_name,
               'player_stats': player_stats,
               'player_id': player_id,
               'player_bio': player_bio
               }

    return render(request, 'nba_stats/post_season.html', context=context)


# regular season rankings
def regular_season_rankings(request, player_full_name, player_id):
    # Get player headshot
    player_headshot = get_player_image(player_id, player_full_name)

    # Get regular season rankings
    player_stats = rankings_regular_season(player_id)

    # get player bio
    player_bio = get_player_bio(player_full_name)

    context = {'player_headshot': player_headshot,
               'player_full_name': player_full_name,
               'player_stats': player_stats,
               'player_id': player_id,
               'player_bio': player_bio,
               }

    return render(request, 'nba_stats/regular_season_rankings.html', context=context)


# post season rankings
def post_season_rankings(request, player_full_name, player_id):
    # Get player headshot
    player_headshot = get_player_image(player_id, player_full_name)

    # Get post season rankings
    player_stats = rankings_post_season(player_id)

    # get player bio
    player_bio = get_player_bio(player_full_name)

    context = {'player_headshot': player_headshot,
               'player_full_name': player_full_name,
               'player_stats': player_stats,
               'player_id': player_id,
               'player_bio': player_bio
               }

    return render(request, 'nba_stats/post_season_rankings.html', context=context)


def compare_players(request):
    if request.method == 'POST':
        form = PlayerCompareForm(request.POST)
        if form.is_valid():
            # Get the player name from the form's cleaned data
            player1 = form.cleaned_data['player1']
            player1.title()  # NBA API is case sensitive

            player2 = form.cleaned_data['player2']
            player2.title()

            # Use the NBA API to find the player's ID based on the name
            player1_info = players.find_players_by_full_name(player1)
            player2_info = players.find_players_by_full_name(player2)

            # Redirect to the search results page if both player are valid
            if player1_info and player2_info:
                player1_id = player1_info[0]['id']
                player1_full_name = player1_info[0]['full_name']

                player2_id = player2_info[0]['id']
                player2_full_name = player2_info[0]['full_name']

                # store players info into a list
                players_info = [player1_id, player2_id, player1_full_name, player2_full_name]

                # store players info in a session for use in next view
                request.session['players_info'] = players_info

                return redirect('nba_stats:compare_profiles')
            else:
                # If player not found, show an error message or handle it as needed
                # For simplicity, we'll just redirect back to the search form with an error message
                return redirect('nba_stats:compare_players')
    else:
        form = PlayerCompareForm()

    context = {'form': form}

    return render(request, "nba_stats/compare_search.html", context)


# view for comparison home page
def compare_profiles(request):
    # get players info from session
    players_info = request.session.get('players_info')

    # get player IDs
    player1_id = players_info[0]
    player2_id = players_info[1]

    # Get player names
    player1_full_name = players_info[2]
    player2_full_name = players_info[3]

    # get players headshots
    player1_headshot = get_player_image(player1_id, player1_full_name)
    player2_headshot = get_player_image(player2_id, player2_full_name)

    # Get players yearly stats
    player1_stats = player_career_numbers(player1_id)
    player2_stats = player_career_numbers(player2_id)

    # getting per game averages
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

        # stats dropdown form
    form = StatsCompForm()

    if request.method == 'POST':
        form = StatsCompForm(request.POST)

        # get selected option
        if form.is_valid():
            comp_option = form.cleaned_data['option']
            title = form.get_graph_title(comp_option)
            graph = get_graph(player1_id, player1_full_name, player2_id, player2_full_name, comp_option, title)

            # Append graph to players info list and store in session for use in next view
            # This list will hold all the info we need for the comparison view
            comparison_info = [player1_id, player2_id, player1_headshot, player2_headshot, player1_full_name,
                               player2_full_name, graph]
            request.session['comparison_info'] = comparison_info
            return redirect('nba_stats:show_graph')

        else:
            return redirect('nba_stats:compare_players')

    context = {'player1_headshot': player1_headshot,
               'player2_headshot': player2_headshot,
               'player1_full_name': player1_full_name,
               'player2_full_name': player2_full_name,
               'player1_stats': player1_stats,
               'player2_stats': player2_stats,
               'player1_id': players_info[0],
               'player2_id': players_info[1],
               'form': form
               }

    return render(request, "nba_stats/comparison.html", context)


# This view will show the comparison graph for the two players
def show_graph(request):
    # Get players
    comparison_info = request.session.get('comparison_info')

    # get player IDs
    player1_id = comparison_info[0]
    player2_id = comparison_info[1]

    # get players headshots
    player1_headshot = comparison_info[2]
    player2_headshot = comparison_info[3]

    # Get player names
    player1_full_name = comparison_info[4]
    player2_full_name = comparison_info[5]

    # Get graph
    graph = comparison_info[6]

    context = {'player1_headshot': player1_headshot,
               'player2_headshot': player2_headshot,
               'player1_full_name': player1_full_name,
               'player2_full_name': player2_full_name,
               'graph': graph,
               'player1_id': player1_id,
               'player2_id': player2_id,
               }

    return render(request, "nba_stats/graph_comparison.html", context)
