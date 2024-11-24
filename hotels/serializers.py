from rest_framework import serializers
from .models import *


class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = ['id', 'title', 'image', 'job_time', 'address']


class Hotel_informationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel_information
        fields = '__all__'  # Serialize all fields of the model