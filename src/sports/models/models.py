from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, null=True, blank=True)
    olympic_sport = models.BooleanField(default=False)
    origin_country = models.CharField(max_length=50, null=True, blank=True)
    first_appearance = models.IntegerField(null=True, blank=True)
    team_sport = models.BooleanField(default=False)
    number_of_players = models.IntegerField(null=True, blank=True)
    governing_body = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class FamousAthlete(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='athletes')
    titles = models.IntegerField(default=0)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    active = models.BooleanField(default=True)
    records = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

