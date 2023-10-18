from django.shortcuts import render, redirect
from .forms import PlayerSearchForm, StatsDropdownForm, PlayerCompareForm
from nba_api.stats.static import players
from .functions import player_career_numbers, get_player_image, player_regular_season, player_post_season, \
    rankings_regular_season, rankings_post_season


def player_search(request):
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
                # If player not found, show an error message or handle it as needed
                # For simplicity, we'll just redirect back to the search form with an error message
                return redirect('nba_stats:player_search')
    else:
        form = PlayerSearchForm()

    context = {'form': form}

    return render(request, 'nba_stats/player_search.html', context=context)


def player_details(request, player_full_name, player_id):
    # get player headshot
    player_headshot = get_player_image(player_id)

    # Get player career stats
    player_stats = player_career_numbers(player_id)

    # getting per game averages
    for season_data in player_stats:

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
               'form': form
               }

    return render(request, 'nba_stats/career_stats.html', context=context)


# regular season totals
def regular_season(request, player_full_name, player_id):
    # Get player headshot
    player_headshot = get_player_image(player_id)

    # Get players yearly numbers
    player_stats = player_regular_season(player_id)

    # getting per game averages
    for season_data in player_stats:

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

    context = {'player_headshot': player_headshot,
               'player_full_name': player_full_name,
               'player_stats': player_stats,
               'player_id': player_id,
               }

    return render(request, 'nba_stats/regular_season.html', context=context)


# post season totals
def post_season(request, player_full_name, player_id):
    # Get player headshot
    player_headshot = get_player_image(player_id)

    # Get players yearly numbers
    player_stats = player_post_season(player_id)

    # getting per game averages
    for season_data in player_stats:

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

    context = {'player_headshot': player_headshot,
               'player_full_name': player_full_name,
               'player_stats': player_stats,
               'player_id': player_id
               }

    return render(request, 'nba_stats/post_season.html', context=context)


# regular season rankings
def regular_season_rankings(request, player_full_name, player_id):
    # Get player headshot
    player_headshot = get_player_image(player_id)

    # Get regular season rankings
    player_stats = rankings_regular_season(player_id)

    context = {'player_headshot': player_headshot,
               'player_full_name': player_full_name,
               'player_stats': player_stats,
               'player_id': player_id
               }

    return render(request, 'nba_stats/regular_season_rankings.html', context=context)


# post season rankings
def post_season_rankings(request, player_full_name, player_id):
    # Get player headshot
    player_headshot = get_player_image(player_id)

    # Get post season rankings
    player_stats = rankings_post_season(player_id)

    context = {'player_headshot': player_headshot,
               'player_full_name': player_full_name,
               'player_stats': player_stats,
               'player_id': player_id
               }

    return render(request, 'nba_stats/post_season_rankings.html', context=context)

# still working on this view
def compare_players(request):
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
                # If player not found, show an error message or handle it as needed
                # For simplicity, we'll just redirect back to the search form with an error message
                return redirect('nba_stats:player_search')
    else:
        form = PlayerSearchForm()

    context = {'form': form}


    new_form = PlayerCompareForm()
    player_list = []  # each player will be appended to this list
    context = {}

    if request.method == 'POST':
        new_form = PlayerCompareForm(request.POST)

        player1 = request.POST.get('player1')
        player_list.append(player1)

        player2 = request.POST.get('player2')
        player_list.append(player2)

        request.session['artist_list'] = artist_list
        return redirect('vibe_check')  # redirect to vibe_check

    context.update({'vibe_form': new_form})

    return render(request, 'playlist/vibe_check.html', context=context)
