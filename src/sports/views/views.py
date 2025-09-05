from rest_framework import viewsets
from ..models.models import FamousAthlete, Sport
from ..serializers.serializers import FamousAthleteSerializer, SportSerializer

class FamousAthleteViewSet(viewsets.ModelViewSet):
    queryset = FamousAthlete.objects.all()
    serializer_class = FamousAthleteSerializer

class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer