from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, null=True, blank=True)
    olympic_sport = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class FamousAthlete(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='athletes')
    titles = models.IntegerField(default=0)

    def __str__(self):
        return self.name
