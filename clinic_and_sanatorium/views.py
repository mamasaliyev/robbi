from rest_framework import generics
from .models import clinic, clinic_and_sanatorium
from .serializers import ClinicSerializer, ClinicAndSanatoriumSerializer
from rest_framework.permissions import IsAuthenticated

class ClinicListCreateAPIView(generics.ListCreateAPIView):
    queryset = clinic.objects.all()
    serializer_class = ClinicSerializer
    permission_classes = [IsAuthenticated]


class ClinicAndSanatoriumListCreateAPIView(generics.ListCreateAPIView):
    queryset = clinic_and_sanatorium.objects.all()
    serializer_class = ClinicAndSanatoriumSerializer