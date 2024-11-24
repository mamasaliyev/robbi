from rest_framework import serializers
from .models import Parks, Parks_info


class ParksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parks
        fields = '__all__'

class ParksInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parks_info
        fields = '__all__'