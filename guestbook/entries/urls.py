from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EntriesViewSet

router = DefaultRouter()
router.register(r'entries', EntriesViewSet, basename='entry')
app_name = 'entries'

urlpatterns = router.urls