from django.urls import path
from .views import ClinicListCreateAPIView, ClinicAndSanatoriumListCreateAPIView

urlpatterns = [
    path('clinics/', ClinicListCreateAPIView.as_view(), name='clinic-list-create'),
    path('clinics-and-sanatoriums/', ClinicAndSanatoriumListCreateAPIView.as_view(), name='clinic-and-sanatorium-list-create'),
]