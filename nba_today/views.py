from django.shortcuts import render
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

    context = {
        'results': results
    }

    return render(request, 'nba_today/game_results.html', context=context)


def game_leaders(request, num):

    #game_num = num + 1
    results = get_scores()
    leaders = results[num]['gameLeaders']

    # get player headshots
    home_player_id = leaders['homeLeaders']['personId']
    home_player_name = leaders['homeLeaders']['name']

    away_player_id = leaders['awayLeaders']['personId']
    away_player_name = leaders['awayLeaders']['name']

    home_player_image = get_player_image(home_player_id, home_player_name)
    away_player_image = get_player_image(away_player_id, away_player_name)

    context = {
        'results': results,
        'home_player_image': home_player_image,
        'home_player_name': home_player_name,
        'away_player_name': away_player_name,
        'away_player_image': away_player_image,
        'away_player_id': away_player_id,
        'home_player_id': home_player_id

    }

    return render(request, 'nba_today/game_leaders.html', context=context)


