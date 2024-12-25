from rest_framework import generics
from .models import clinic, clinic_and_sanatorium
from .serializers import ClinicSerializer, ClinicAndSanatoriumSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Clinic uchun List va Create API View
class ClinicListCreateAPIView(generics.ListCreateAPIView):
    queryset = clinic.objects.all()
    serializer_class = ClinicSerializer
    # Faqatgina autentifikatsiyadan o'tgan foydalanuvchilar POST so'rov yuborishi mumkin, GET esa ochiq
    permission_classes = [IsAuthenticatedOrReadOnly]


# Clinic va Sanatorium uchun List va Create API View
class ClinicAndSanatoriumListCreateAPIView(generics.ListCreateAPIView):
    queryset = clinic_and_sanatorium.objects.all()
    serializer_class = ClinicAndSanatoriumSerializer
    # Faqatgina autentifikatsiyadan o'tgan foydalanuvchilar POST so'rov yuborishi mumkin, GET esa ochiq
    permission_classes = [IsAuthenticatedOrReadOnly]
