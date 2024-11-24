
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import Hotel_informationSerializer
from rest_framework import generics
from rest_framework import viewsets
from .serializers import HotelsSerializer
from django_filters import rest_framework as filters


class HotelsFilter(filters.FilterSet):
    address = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Hotels
        fields = ['address']

class HotelsViewSet(viewsets.ModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HotelsFilter


class Hotel_informationView(APIView):
    def get(self, request):
        # Retrieve all hotel (Hotel_information)
        hotel = Hotel_information.objects.all()
        serializer = Hotel_informationSerializer(hotel, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new hotel (Hotel_information)
        serializer = Hotel_informationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new hotel instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Hotel_informationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel_information.objects.all()
    serializer_class = Hotel_informationSerializer
