from rest_framework import serializers
from .models import Mosques, PrayerTimes


class PrayerTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerTimes
        fields = ['id', 'mosque', 'bomdod', 'quyosh', 'peshin', 'asr', 'shom', 'xufton', 'date']


class MosquesSerializer(serializers.ModelSerializer):
    prayer_times = PrayerTimesSerializer(many=True, read_only=True)

    class Meta:
        model = Mosques
        fields = ['id', 'title', 'jop_time', 'image', 'address', 'latitude', 'longitude', 'tel', 'prayer_times']
