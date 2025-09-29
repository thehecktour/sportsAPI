from rest_framework import serializers
from ..models.models import FamousAthlete, Sport, Record


class FamousAthleteSerializer(serializers.ModelSerializer):
    sport = serializers.StringRelatedField() 

    class Meta:
        model = FamousAthlete
        fields = '__all__'


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    athlete = serializers.StringRelatedField()
    sport = serializers.StringRelatedField()
    
    class Meta:
        model = Record
        fields = '__all__'
