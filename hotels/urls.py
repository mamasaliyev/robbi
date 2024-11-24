
from django.urls import path, include
from .views import Hotel_informationView, Hotel_informationDetailView
from rest_framework.routers import DefaultRouter
from hotels.views import HotelsViewSet


router = DefaultRouter()
router.register(r'hotels', HotelsViewSet)

urlpatterns = [
    path('hotels/', include(router.urls)),
    path('hotel_information/', Hotel_informationView.as_view(), name='hotel-list'),  # List and create hotel
    path('hotel/<int:pk>/', Hotel_informationDetailView.as_view(), name='hotel-detail'),

]
