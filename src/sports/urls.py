from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.views import FamousAthleteViewSet, SportViewSet

router = DefaultRouter()
router.register(r'famous-athletes', FamousAthleteViewSet, basename='famous-athletes')
router.register(r'sports', SportViewSet, basename='sports')

urlpatterns = [
    path("", include(router.urls)),
]
