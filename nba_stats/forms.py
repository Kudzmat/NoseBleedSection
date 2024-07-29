from django import forms
from django.core import validators

STAT_OPTIONS = (
    ('--- Stats By Year ---', '--- Stats By Year  ---'),
    ('Reg. Season', 'Reg. Season'),
    ('Post Season', 'Post Season'),
    ('Reg. Season Rankings', 'Reg. Season Rankings'),
    ('Post Season Rankings', 'Post Season Rankings'),

)

# tuple where the first element is the value stored in the dictionary, and the second element is the user-readable
# option.
COMP_OPTIONS = (
    ('--- Compare Stats By Season ---', '--- Compare Stats By Season ---'),
    ('PPG', 'Points Per Game'),
    ('RPG', 'Rebs Per Game'),
    ('APG', 'Assists Per Game'),
    ('BLKPG', 'Blocks Per Game'),
    ('STLPG', 'Steals Per Game'),
    ('FG_PCT', 'Field Goal %'),
    ('FG3_PCT', '3 Point %'),
    ('FT_PCT', 'Free Thrown%'),
    ('GP', 'Games Played'),
    ('GS', 'Games Started'),
    ('MIN', 'Minutes')
)


# form for searching a player
class PlayerSearchForm(forms.Form):
    player_name = forms.CharField(
        label='',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter player name',
                'class': 'form-control',
                'aria-label': 'Player Name'
            }
        ),
        error_messages={
            'required': 'Please enter a player name.',
            'max_length': 'Player name cannot exceed 100 characters.'
        }
    )

# form for getting more stats
class StatsDropdownForm(forms.Form):
    option = forms.ChoiceField(choices=STAT_OPTIONS, label="")


# form for stats comparison
class StatsCompForm(forms.Form):
    option = forms.ChoiceField(choices=COMP_OPTIONS, label="")

    # this method will allow me to get the selected option's readable value to use for the graph's title
    def get_graph_title(self, selected_option):
        for dict_value, reader_value in COMP_OPTIONS:
            if dict_value == selected_option:
                title = reader_value

        return title


# form for artist search
class PlayerCompareForm(forms.Form):
    player1 = forms.CharField(
        validators=[validators.MaxLengthValidator(50), validators.MinLengthValidator(1)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter Player 1', 'style': 'width:300px'}))

    player2 = forms.CharField(
        validators=[validators.MaxLengthValidator(50), validators.MinLengthValidator(1)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter Player 2', 'style': 'width:300px'}))
