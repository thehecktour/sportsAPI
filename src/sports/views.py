from rest_framework import viewsets
from .models import FamousAthlete
from .serializers import FamousAthleteSerializer

class FamousAthleteViewSet(viewsets.ModelViewSet):
    queryset = FamousAthlete.objects.all()
    serializer_class = FamousAthleteSerializer
