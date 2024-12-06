from rest_framework.generics import ListCreateAPIView
from .models import Mosques
from .serializers import MosquesSerializer
from rest_framework import generics
from .models import PrayerTimes
from .serializers import PrayerTimesSerializer


class MosquesListCreateAPIView(ListCreateAPIView):
    queryset = Mosques.objects.all()
    serializer_class = MosquesSerializer



# PrayerTimes ro'yxatini olish va yangi vaqtlar qo'shish uchun
class PrayerTimesListCreateAPIView(generics.ListCreateAPIView):
    queryset = PrayerTimes.objects.all()
    serializer_class = PrayerTimesSerializer

