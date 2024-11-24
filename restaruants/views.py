
# views.py
from rest_framework import viewsets
from .models import Restaurants, Restaurant_info, Menu
from .serializers import RestaurantSerializer, RestaurantInfoSerializer, MenuSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantInfoViewSet(viewsets.ModelViewSet):
    queryset = Restaurant_info.objects.all()
    serializer_class = RestaurantInfoSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
