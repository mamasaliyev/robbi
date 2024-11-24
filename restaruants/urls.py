
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, RestaurantInfoViewSet, MenuViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')
router.register(r'restaurant-info', RestaurantInfoViewSet, basename='restaurantinfo')
router.register(r'menu', MenuViewSet, basename='menu')

urlpatterns = [
    path('restaurants/', include(router.urls)),
]
