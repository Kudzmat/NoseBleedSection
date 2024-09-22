from django.db import models


class EasternConferenceTeams(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_full_name = models.CharField(max_length=100, default="N/A")
    team_name = models.CharField(max_length=100, default="N/A")
    team_abbreviated = models.CharField(max_length=10, default="N/A")
    team_city = models.CharField(max_length=100, default="N/A")
    team_logo_url = models.URLField(blank=True, null=True,
                                    default="https://media.licdn.com/dms/image/v2/C4E0BAQEke_OTftxqtQ/company-logo_200_200/company-logo_200_200/0/1660575300584/national_basketball_association_logo?e=1733356800&v=beta&t=LJiOxzNM9mfdgbHT2akuXDP2oYH3YUMDpypmkObMSyc")
    team_colour = models.CharField(max_length=10, default="N/A")  # Hex color code

    def __str__(self):
        return self.team_full_name

    class Meta:
        verbose_name_plural = "Eastern Conference Teams"


class WesternConferenceTeams(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_full_name = models.CharField(max_length=100, default="N/A")
    team_name = models.CharField(max_length=100, default="N/A")
    team_abbreviated = models.CharField(max_length=10, default="N/A")
    team_city = models.CharField(max_length=100, default="N/A")
    team_logo_url = models.URLField(blank=True, null=True,
                                    default="https://media.licdn.com/dms/image/v2/C4E0BAQEke_OTftxqtQ/company-logo_200_200/company-logo_200_200/0/1660575300584/national_basketball_association_logo?e=1733356800&v=beta&t=LJiOxzNM9mfdgbHT2akuXDP2oYH3YUMDpypmkObMSyc")
    team_colour = models.CharField(max_length=10, default="N/A")  # Hex color code

    def __str__(self):
        return self.team_full_name

    class Meta:
        verbose_name_plural = "Western Conference Teams"


# class TeamHistory(models.Model):
#     team_id = models.IntegerField(primary_key=True)
#     team_name = models.CharField(max_length=100)
#     arena = models.CharField(max_length=100)
#     coach = models.CharField(max_length=100)
#     trophies = models.JSONField(default=list, blank=True)
#
#     def __str__(self):
#         return f"{self.team_name} History"


class RetiredPlayers(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=100)
    players = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.team_name} Retired Players"

#
# class CurrentRoster(models.Model):
#     team_id = models.IntegerField(primary_key=True)
#     team_name = models.CharField(max_length=100)
#     roster = models.JSONField(default=list, blank=True)
#
#     def __str__(self):
#         return f"{self.team_name} Current Roster"
#
# #
# class TeamRankings(models.Model):
#     team_id = models.IntegerField(primary_key=True)
#     team_name = models.CharField(max_length=100)
#     rankings = models.JSONField(default=dict, blank=True)
#
#     def __str__(self):
#         return f"{self.team_name} Rankings"
