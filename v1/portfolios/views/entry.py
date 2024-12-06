from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from ..models import PoolInvestmentPortfolioEntry, ClientPortfolioEntry
from ..serializers.entry import PoolInvestmentPortfolioEntrySerializer, ClientPortfolioEntrySerializer


class PoolInvestmentPortfolioEntryViewSet(ModelViewSet):
    serializer_class = PoolInvestmentPortfolioEntrySerializer
    queryset = PoolInvestmentPortfolioEntry.objects.all()
    permission_classes = [AllowAny]


class ClientPortfolioEntryViewSet(ModelViewSet):
    serializer_class = ClientPortfolioEntrySerializer
    queryset = ClientPortfolioEntry.objects.all()
    permission_classes = [AllowAny]
