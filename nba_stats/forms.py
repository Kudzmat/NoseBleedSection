from django import forms
from django.core import validators

STAT_OPTIONS = (
    ('--- View More Stats ---', '--- View More Stats ---'),
    ('Reg. Season Totals', 'Reg. Season Totals'),
    ('Post Season Totals', 'Post Season Totals'),
    ('Reg. Season Rankings', 'Reg. Season Rankings'),
    ('Post Season Rankings', 'Post Season Rankings'),

)


# form for searching a player
class PlayerSearchForm(forms.Form):
    player_name = forms.CharField(label='Player Name', max_length=100)


# form for getting more stats
class StatsDropdownForm(forms.Form):
    option = forms.ChoiceField(choices=STAT_OPTIONS, label="")
