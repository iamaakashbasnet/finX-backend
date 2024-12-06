from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import PoolInvestmentPortfolio, ClientPortfolio
from ..serializers import PoolInvestmentPortfolioSerializer, ClientPortfolioSerializer


class PoolInvestmentPortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PoolInvestmentPortfolioSerializer
    queryset = PoolInvestmentPortfolio.objects.all()
    permission_classes = [AllowAny]


class ClientPortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = ClientPortfolioSerializer
    queryset = ClientPortfolio.objects.all()
    permission_classes = [AllowAny]
