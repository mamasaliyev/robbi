from rest_framework import serializers
from .models import clinic, clinic_and_sanatorium

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = clinic
        fields = '__all__'  # Include all fields or specify a list of fields

class ClinicAndSanatoriumSerializer(serializers.ModelSerializer):
    class Meta:
        model = clinic_and_sanatorium
        fields = '__all__'