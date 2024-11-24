
from rest_framework import serializers
from .models import Restaurants, Restaurant_info, Menu

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = '__all__'

class RestaurantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_info
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
