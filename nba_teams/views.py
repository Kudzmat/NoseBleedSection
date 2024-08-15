from django.shortcuts import render, redirect
from .functions import *


def team_page(request, team_name):
    # team logo and other information
    team_info = get_team(team_name)
    team_id = team_info[0]

    # championships and current relevant info
    team_history = get_team_history(team_id)
    current_info = team_history[0]
    championships = team_history[1]

    # retired players
    retired = retired_players(team_id)

    # team ranks
    team_ranks = get_team_rankings(team_id)

    # team_roster
    roster = get_team_roster(team_id)

    context = {
        'team_info': team_info,
        'team_id': team_id,
        'current_info ': current_info,
        'championships': championships,
        'retired': retired,
        'team_ranks': team_ranks,
        'roster': roster
    }

    return render(request, 'nba_teams/team_page.html', context=context)
