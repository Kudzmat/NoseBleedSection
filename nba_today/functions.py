from nba_api.live.nba.endpoints import scoreboard
import pprint


# get today's game scores
def get_scores():
    # Today's Score Board
    games = scoreboard.ScoreBoard()
    results = scoreboard.ScoreBoard().games.get_dict()

    return results

    #pprint.pprint(results[0]['awayTeam'])
