from django.shortcuts import render
from .functions import get_scores, get_team_image


def nba_results(request):
    results = get_scores()

    for game in results:
        # Get home teams logos
        team_id = game['homeTeam']['teamId']
        team_name = game['homeTeam']['teamTricode']
        # Get team logo
        home_logo = get_team_image(team_id, team_name)

        # save team logo to results
        game['homeTeam']['teamLogo'] = home_logo

        # Get away teams logos
        team_id = game['awayTeam']['teamId']
        team_name = game['awayTeam']['teamTricode']
        # Get team logo
        away_logo = get_team_image(team_id, team_name)

        # save team logo to results
        game['awayTeam']['teamLogo'] = away_logo

    context = {
        'results': results
    }

    return render(request, 'nba_today/game_results.html', context=context)
