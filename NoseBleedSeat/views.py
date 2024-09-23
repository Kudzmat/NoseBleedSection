from django.shortcuts import render, redirect
from nba_stats.forms import PlayerSearchForm, TeamSearchForm
from nba_api.stats.static import players
from nba_stats.models import *
from .functions import *
from nba_stats.functions import *
from nba_teams.functions import get_team
from .forms import PlayerOneForm, PlayerTwoForm
from nba_teams.models import *
import random

WORDS = [
    "I don’t always talk stats, but when I do, I drop dimes.",
    "You miss 100% of the shots... you never analyze.",
    "Life’s too short for bad shots and weak stats.",
    "Talk stats to me, baby!",
    "I break down the game like a defender on skates.",
    "Got handles? Try handling these numbers.",
    "Ball don’t lie – and neither do the stats.",
    "My stats are like a triple-double – versatile and game-changing.",
    "No fouls here, just hard-hitting facts.",
    "If you’re not crunching stats, are you even watching the game?",
    "Hoop dreams powered by stats.",
    "Breaking ankles and breaking down numbers.",
    "Rebounds are cool, but rebounding from bad data is cooler.",
    "Analyze the court like a coach with a clipboard.",
    "I don’t throw bricks, just straight facts.",
    "My range? From half-court to the spreadsheet.",
    "The ball is in your court, just don’t ignore the data.",
    "Not all heroes wear jerseys – some crunch the numbers.",
    "Dribbling through data like Kyrie through defenders.",
    "More stats than an NBA All-Star game.",
    "Stats so sharp, they cut through the defense.",
    "No need to trash talk when you’ve got the numbers.",
    "Swish! That’s the sound of a perfect stat.",
    "Taking basketball geekery to the next level.",
    "Want to talk hoops? Let’s start with the data.",
    "Every shot tells a story, and we’ve got the whole book.",
    "Step into the zone where stats meet strategy.",
    "On the court or in the data, I’m always in the zone.",
    "Throwing numbers like Steph throws threes.",
    "Stats as reliable as a free throw – well, most free throws.",
    "Got a favorite player? Let the numbers do the talking.",
    "Crossovers are cool, but have you tried a stat breakdown?",
    "I’ve got game... and numbers to back it up.",
    "Want to compare legends? I’ve got the data for that.",
    "Stats are like assists – they make everything better.",
    "No stat padding here, just the real numbers.",
    "I ball out in stats, not just in games.",
    "Stats so slick, they should be illegal in the paint.",
    "Dropping dimes on the court and with the data.",
    "Call me the point guard of stats – I set you up to win.",
    "More efficient than a pick and roll.",
    "Breaking down the game like a zone defense.",
    "If you don’t love stats, you’re missing the real game.",
    "I don’t post up, I post stats.",
    "I might not dunk, but my stats slam down hard.",
    "The stat sheet is my playbook.",
    "Basketball IQ? Check. Stat IQ? Even better.",
    "Don’t just play the game, understand it.",
    "Just like a fast break, stats can turn the game around.",
    "From the court to the calculator – I’m always analyzing.",
    "I see the game in numbers and patterns.",
    "Good defense stops shots, great stats tell why.",
    "Making the numbers dance like I’m James Harden.",
    "Stats so smooth, you’ll think they were a finger roll.",
    "I got that Mamba mentality... for stats.",
    "Not all data is created equal, and I’m here for the elite numbers.",
    "I don’t play iso, I play team ball – with stats!",
    "Analytics MVP, coming through.",
    "Shooting threes? I’m shooting stats.",
    "You can run plays, I run numbers.",
    "The best assist is giving you the best stats.",
    "Crossing over between basketball and analytics.",
    "Like a buzzer-beater, I bring clutch stats.",
    "I don't call for a screen, I call for the stat sheet.",
    "Offense wins games, stats win arguments.",
    "I break down the game faster than a fast break.",
    "Every player has a story, and the stats write it.",
    "Dropping knowledge like a step-back jumper.",
    "Stealing stats like I’m picking pockets on defense.",
    "Got questions about the game? Stats have the answers.",
    "I don’t do load management, I manage the data.",
    "My shot selection? Data-driven.",
    "In basketball, the scoreboard matters – in stats, every detail does.",
    "Every shot counts, every stat matters.",
    "Less fluff, more numbers.",
    "Stats so accurate, they should be in the Hall of Fame.",
    "I’m not just a basketball geek, I’m a stat geek.",
    "From tip-off to final buzzer, I’ve got the numbers covered.",
    "I ball out in the paint and in the stats.",
    "This is where the real basketball nerds hang out.",
    "No turnover here – just pure data.",
    "I crunch numbers like Shaq in the post.",
    "Don’t need a replay – I’ve got the stats.",
    "Data doesn’t miss, just like MJ in the clutch.",
    "Raining down stats like they’re threes.",
    "Got stats? Let’s break them down together.",
    "I don’t do highlight reels, I do stat reels.",
    "Reading the game like a stat-filled book.",
    "Taking basketball analytics to the next level.",
    "If you’re looking for a slam dunk, check out these stats.",
    "Can’t spell 'basketball' without 'stats.'",
    "Real ballers know the importance of the stat sheet.",
    "When in doubt, check the data.",
    "Fast breaks are great, but fast stats are better.",
    "Behind every great player is a great stat line.",
    "I don’t play the game, I analyze it.",
    "Numbers don’t lie, but bad takes do.",
    "When the game gets tough, the stats get tougher.",
    "I see stats the way others see dunks.",
    "No shot is complete without the numbers to back it up.",
    "Defense wins games, but stats win arguments.",
    "Hoops talk is cool, but stat talk is where it’s at.",
    "You can run the floor, I’ll run the stats.",
    "Running the game one stat at a time.",
    "I’m a stat nerd, and I’m proud of it.",
    "From courtside to inside the data.",
    "Where shots meet stats.",
    "Call me the stat whisperer.",
    "I’m in the paint, breaking down the numbers.",
    "Dropping knowledge like a Steph Curry three.",
    "Stats so cold, they should come with ice packs.",
    "I don’t just watch the game, I dissect it.",
    "I’m always in the zone – the stat zone.",
    "Got a hot take? Let’s see if the stats back it up.",
    "Stats are my playbook, and I’m calling the shots.",
    "I’ve got the numbers you need to win the argument.",
    "Post moves? I’ve got post stats.",
    "Ready to swish stats like a deep three.",
    "Hoop dreams meet stat geek reality.",
    "I’ve got a stat line for every debate.",
    "From the hardwood to the stat sheet.",
    "No game plan is complete without the numbers.",
    "Step into the paint, and into the data.",
    "If stats were shots, I’d never miss.",
    "I analyze stats like I’m calling the game.",
    "You might play the game, but I read the stats.",
    "No bad takes, just pure stats.",
    "Every stat tells a part of the story.",
    "Buzzer beaters are cool, but crunching numbers is better.",
    "Breaking down the game one stat at a time.",
    "Stats so good, you’ll be calling for an encore.",
    "Defense wins championships, stats win arguments.",
    "If you’re not geeking out over stats, are you really a fan?",
    "I’m shooting for accuracy – in stats, not just shots.",
    "Got a problem with your stats? Let’s break it down.",
    "The stat sheet is my highlight reel.",
    "On the court or in the data, I’m always winning.",
    "Call me the stat keeper – I’ve got the game on lock.",
    "If stats were buckets, I’d be leading the league.",
    "Breaking the game down, one possession at a time.",
    "I’m the MVP of basketball stats.",
    "Let’s run the numbers and see who wins.",
    "Crushing numbers like I’m crashing the boards.",
    "You can’t argue with these stats.",
    "The game starts with the numbers.",
    "Every possession matters, just like every stat.",
    "I don’t throw bricks, just straight facts.",
    "Numbers never sleep – and neither do I.",
    "Crunching stats like a rebound in traffic.",
    "From layups to long-range stats.",
    "I’m always on offense – in stats.",
    "Breaking down every possession, one stat at a time.",
    "I’m in the zone – the stat zone.",
    "You can shoot threes, I shoot stats.",
    "Defense might win games, but stats win minds.",
    "I’m on a fast break – in the stat sheet.",
    "Got a stat sheet? I’ll break it down."]

def home(request):

    word_of_the_day = random.choice(WORDS)

    # Delete session data
    request.session.pop('player_page_info', None)
    request.session.pop('player_info', None)
    request.session.pop('player_compare_info', None)



    player_compare_info = []
    player1 = request.session.get('player1', "Lebron james")
    player2 = request.session.get('player2', 'Michael jordan')

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
                del player_bio['_state']  # to avoid TypeError

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
        'word_of_the_day': word_of_the_day
    }

    return render(request, "index.html", context=context)


def about(request):
    player_form = PlayerSearchForm()
    context = {
        'player_form': player_form,

    }
    return render(request, "about.html", context=context)