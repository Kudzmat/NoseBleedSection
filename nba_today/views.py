from django.shortcuts import render

from nba_stats.forms import PlayerSearchForm
from .functions import get_scores, get_team_image
from nba_stats.functions import get_player_image


def nba_results(request):
    results = get_scores()

    for num, game in enumerate(results):
        # Get home teams logos
        team_id = game['homeTeam']['teamId']
        team_name = game['homeTeam']['teamTricode']
        # Get team logo
        home_logo = get_team_image(team_id, team_name)

        # save team logo and game number to results
        # Game num will be used to retrieve game leaders for each game
        game['homeTeam']['teamLogo'] = home_logo
        game['homeTeam']['gameNum'] = num

        # Get away teams logos
        team_id = game['awayTeam']['teamId']
        team_name = game['awayTeam']['teamTricode']
        # Get team logo
        away_logo = get_team_image(team_id, team_name)

        # save team logo and game number to results
        game['awayTeam']['teamLogo'] = away_logo
        game['awayTeam']['gameNum'] = num

    # search form
    player_form = PlayerSearchForm()

    context = {
        'player_form': player_form,
        'results': results
    }

    return render(request, 'nba_today/game_results.html', context=context)


def game_leaders(request, num):
    # Get requested game by index
    results = get_scores()
    my_game = results[num]

    # Get game leaders
    leaders = my_game['gameLeaders']

    # Get player ids and names
    home_player_id = leaders['homeLeaders']['personId']
    home_player_name = leaders['homeLeaders']['name']

    away_player_id = leaders['awayLeaders']['personId']
    away_player_name = leaders['awayLeaders']['name']

    # get player headshots
    home_player_image = get_player_image(home_player_id, home_player_name)
    away_player_image = get_player_image(away_player_id, away_player_name)

    # Get team names
    home_team = leaders['homeLeaders']['teamTricode']
    away_team = leaders['awayLeaders']['teamTricode']

    # Get team logos
    home_team_id = my_game['homeTeam']['teamId']
    home_team_logo = get_team_image(home_team_id, home_team)

    away_team_id = my_game['awayTeam']['teamId']
    away_team_logo = get_team_image(away_team_id, away_team)

    # Get game breakdown
    home_team_scores = my_game['homeTeam']['periods']
    home_final_score = my_game['homeTeam']['score']
    away_team_scores = my_game['awayTeam']['periods']
    away_final_score = my_game['awayTeam']['score']

    # search form
    player_form = PlayerSearchForm()

    context = {
        'player_form': player_form,
        'leaders': leaders,
        'home_player_image': home_player_image,
        'home_player_name': home_player_name,
        'away_player_name': away_player_name,
        'away_player_image': away_player_image,
        'away_player_id': away_player_id,
        'home_player_id': home_player_id,
        'home_team': home_team,
        'away_team': away_team,
        'home_team_logo': home_team_logo,
        'away_team_logo': away_team_logo,
        'home_team_scores': home_team_scores,
        'home_final_score': home_final_score,
        'away_team_scores': away_team_scores,
        'away_final_score': away_final_score
    }

    return render(request, 'nba_today/game_leaders.html', context=context)
