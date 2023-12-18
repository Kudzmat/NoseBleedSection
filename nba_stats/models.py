from django.db import models


# Create your models here.
class PlayerHeadshot(models.Model):
    player_id = models.CharField(unique=True, max_length=50)
    player_name = models.CharField(max_length=50)
    head_shot_url = models.URLField()

    def __str__(self):
        return f"{self.player_name}"
