from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FamousAthleteViewSet

router = DefaultRouter()
router.register(r'famous-athletes', FamousAthleteViewSet, basename='famous-athletes')

urlpatterns = [
    path("", include(router.urls)),
]
