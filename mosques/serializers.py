from rest_framework import serializers
from .models import Mosques, Mosques_info


class MosquesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mosques
        fields = '__all__'

class MosquesInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mosques_info
        fields = '__all__'