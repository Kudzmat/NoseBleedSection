from django.db import models
from django.utils import timezone

# Dictionary for team colors
TEAM_COLOURS = {
    1610612737: '#e03a3e', 1610612738: '#007A33', 1610612751: '#000000', 1610612766: '#00788c',
    1610612749: '#00471b', 1610612754: '#002d62', 1610612748: '#98002e', 1610612755: '#006bb6',
    1610612752: '#f58426', 1610612765: '#c8102e', 1610612757: '#e03a3e', 1610612759: '#c4ced4',
    1610612760: '#007ac1', 1610612758: '#5a2d81', 1610612761: '#ce1141', 1610612762: '#00a9e0',
    1610612740: '#0c2340', 1610612742: '#00538c', 1610612747: '#f9a01b', 1610612743: '#1d428a',
    1610612744: '#ffc72c', 1610612745: '#ce1141', 1610612746: '#1d428a', 1610612763: '#5d76a9',
    1610612750: '#236192', 1610612753: '#0077c0', 1610612756: '#e56020', 1610612764: '#002b5c',
    1610612739: '#860038', 1610612741: '#ce1141'
}

# Dictionary for team names
TEAMS = {
    1610612737: 'Hawks', 1610612738: 'Celtics', 1610612751: 'Nets', 1610612766: 'Hornets', 1610612749: 'Bucks',
    1610612754: 'Pacers', 1610612748: 'Heat', 1610612755: 'Sixers', 1610612752: 'Knicks', 1610612765: 'Pistons',
    1610612757: 'Blazers', 1610612759: 'Spurs', 1610612760: 'Thunder', 1610612758: 'Kings', 1610612761: 'Raptors',
    1610612762: 'Jazz', 1610612740: 'Pelicans', 1610612742: 'Mavericks', 1610612747: 'Lakers',
    1610612743: 'Nuggets', 1610612744: 'Warriors', 1610612745: 'Rockets', 1610612746: 'Clippers',
    1610612763: 'Grizzlies', 1610612750: 'Timberwolves', 1610612753: 'Magic', 1610612756: 'Suns',
    1610612764: 'Wizards', 1610612739: 'Cavaliers', 1610612741: 'Bulls'
}


class PlayerHeadShot(models.Model):
    player_id = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=100, default="N/A")
    player_image_url = models.URLField(default="https://static.vecteezy.com/system/resources/thumbnails/004/511/281/small_2x/default-avatar-photo-placeholder-profile-picture-vector.jpg")
    team_id = models.IntegerField(default=0)
    background_colour = models.CharField(max_length=7, blank=True, null=True, default="N/A")

    def save(self, *args, **kwargs):
        # Set background color based on team_id
        if self.team_id in TEAM_COLOURS:
            self.background_colour = TEAM_COLOURS[self.team_id]
        else:
            self.background_colour = '#FFFFFF'  # Default color if team_id is not in the dictionary
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.player_name} Head Shot"


class PlayerBio(models.Model):
    player_id = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=100, default="N/A")
    school = models.CharField(max_length=100, blank=True, null=True, default="N/A")
    country = models.CharField(max_length=100, blank=True, null=True, default="N/A")
    height = models.CharField(max_length=10, blank=True, null=True, default="N/A")
    weight = models.FloatField(blank=True, null=True, default="N/A")
    year = models.IntegerField(blank=True, null=True, default="N/A")
    number = models.IntegerField(blank=True, null=True, default="N/A")
    position = models.CharField(max_length=50, blank=True, null=True, default="N/A")
    team_id = models.IntegerField(default=0000000000)
    team_name = models.CharField(max_length=50, blank=True, null=True, default="N/A")
    status = models.CharField(max_length=50, blank=True, null=True, default="N/A")
    PTS = models.FloatField(blank=True, null=False, default=0)  # Points per game
    REB = models.FloatField(blank=True, null=False, default=0)  # Rebounds per game
    AST = models.FloatField(blank=True, null=False, default=0)  # Assists per game
    BLK = models.FloatField(blank=True, null=False, default=0)  # Blocks per game
    STL = models.FloatField(blank=True, null=False, default=0)  # Steals per game

    def save(self, *args, **kwargs):
        # Set team name based on team_id
        if self.team_id in TEAMS:
            self.team_name = TEAMS[self.team_id]
        else:
            self.team_name = 'Unknown'  # Default value if team_id is not in the dictionary
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.player_name} Bio"


class CareerAwards(models.Model):
    player_id = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=100, default="N/A")
    accomplishments = models.JSONField(default=dict, blank=True)
    date = models.DateField(default=timezone.now, blank=True)  # Automatically set to today's date

    def __str__(self):
        return f"{self.player_name} Awards. Last Update {self.date}"


class LeagueLeaders(models.Model):
    date = models.DateField(default=timezone.now, blank=True)  # Automatically set to today's date
    leaders = models.JSONField(default=dict)  # Dictionary to store stat leaders

    def __str__(self):
        return f"League Leaders. Last Update {self.date}"




