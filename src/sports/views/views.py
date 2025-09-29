from rest_framework import viewsets
from ..models.models import FamousAthlete, Sport, Record
from ..serializers.serializers import FamousAthleteSerializer, SportSerializer, RecordSerializer


class FamousAthleteViewSet(viewsets.ModelViewSet):
    queryset = FamousAthlete.objects.all()
    serializer_class = FamousAthleteSerializer


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
