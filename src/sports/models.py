from django.db import models

class FamousAthlete(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    sport = models.CharField(max_length=50)
    titles = models.IntegerField(default=0)

    def __str__(self):
        return self.name
