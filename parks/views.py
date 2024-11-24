from rest_framework import viewsets

from parks.models import Parks_info, Parks
from parks.serializers import ParksSerializers, ParksInfoSerializers



class ParksViewSet(viewsets.ModelViewSet):
    queryset = Parks.objects.all()
    serializer_class = ParksSerializers

class ParksInfoViewSet(viewsets.ModelViewSet):
    queryset = Parks_info.objects.all()
    serializer_class = ParksInfoSerializers
