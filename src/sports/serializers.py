from rest_framework import serializers
from .models import FamousAthlete

class FamousAthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamousAthlete
        fields = '__all__'
