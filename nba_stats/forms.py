from django import forms
from django.core import validators

STAT_OPTIONS = (
    ('--- Stats By Year ---', '--- Stats By Year  ---'),
    ('Reg. Season', 'Reg. Season'),
    ('Post Season', 'Post Season'),
    ('Reg. Season Rankings', 'Reg. Season Rankings'),
    ('Post Season Rankings', 'Post Season Rankings'),

)

COMP_OPTIONS = (
    ('--- Stats By Season ---', '--- Stats By Season ---'),
    ('Points Per Game', 'Points Per Game'),
    ('Rebs Per Game', 'Rebs Per Game'),
    ('Assists Per Game', 'Assists Per Game'),
    ('Blocks Per Game', 'Blocks Per Game'),
    ('Steals Per Game', 'Steals Per Game'),
    ('FG%', 'FG%'),
    ('3pt%', '3pt%'),
    ('FT%', 'FT%'),
    ('Games Played', 'Games Played'),
    ('Games Started', 'Games Started'),
    ('Minutes', 'Minutes')

)


# form for searching a player
class PlayerSearchForm(forms.Form):
    player_name = forms.CharField(label='Player Name', max_length=100)


# form for getting more stats
class StatsDropdownForm(forms.Form):
    option = forms.ChoiceField(choices=STAT_OPTIONS, label="")


# form for stats comparison
class StatsCompForm(forms.Form):
    option = forms.ChoiceField(choices=COMP_OPTIONS, label="")


# form for artist search
class PlayerCompareForm(forms.Form):
    player1 = forms.CharField(
        validators=[validators.MaxLengthValidator(50), validators.MinLengthValidator(1)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter Player 1', 'style': 'width:300px'}))

    player2 = forms.CharField(
        validators=[validators.MaxLengthValidator(50), validators.MinLengthValidator(1)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter Player 2', 'style': 'width:300px'}))
