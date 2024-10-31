from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from v1.clients.models import GeneralClient, PoolInvestmentClient
from v1.clients.serializers import GeneralClientSerializer, PoolInvestmentClientSerializer


class GeneralClientViewSet(viewsets.ModelViewSet):
    serializer_class = GeneralClientSerializer
    queryset = GeneralClient.objects.all()
    permission_classes = [IsAuthenticated]


class PoolInvestmentClientViewSet(viewsets.ModelViewSet):
    serializer_class = PoolInvestmentClientSerializer
    queryset = PoolInvestmentClient.objects.all()
    permission_classes = [IsAuthenticated]
