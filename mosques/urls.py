from django.conf.urls.static import static
from django.urls import path
from config import settings
from .views import MosquesListCreateAPIView, PrayerTimesListCreateAPIView

urlpatterns = [
    path('mosques/', MosquesListCreateAPIView.as_view(), name='mosques-list'),
    # PrayerTimes ro'yxati va qo'shish
    path('prayer-times/', PrayerTimesListCreateAPIView.as_view(), name='prayer-times-list'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
