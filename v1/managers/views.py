from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import FirmExecutive, FirmManager
from .serializers import FirmExecutiveSerializer, FirmManagerSerializer


class FirmExecutiveViewSet(viewsets.ModelViewSet):
    serializer_class = FirmExecutiveSerializer
    queryset = FirmExecutive.objects.all()
    permission_classes = [IsAuthenticated]


class FirmManagerViewSet(viewsets.ModelViewSet):
    serializer_class = FirmManagerSerializer
    queryset = FirmManager.objects.all()
    permission_classes = [IsAuthenticated]
