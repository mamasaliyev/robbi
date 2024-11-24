from rest_framework import viewsets

from mosques.models import Mosques, Mosques_info
from mosques.serializers import MosquesSerializers, MosquesInfoSerializers


class MosquesViewSet(viewsets.ModelViewSet):
    queryset = Mosques.objects.all()
    serializer_class = MosquesSerializers

class MosquesInfoViewSet(viewsets.ModelViewSet):
    queryset = Mosques_info.objects.all()
    serializer_class = MosquesInfoSerializers
