from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from v1.portfolios.models import PoolInvestmentPortfolio, ClientPortfolio
from v1.portfolios.serializers import PoolInvestmentPortfolioSerializer, ClientPortfolioSerializer


class PoolInvestmentPortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PoolInvestmentPortfolioSerializer
    queryset = PoolInvestmentPortfolio.objects.all()
    permission_classes = [AllowAny]


class ClientPortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = ClientPortfolioSerializer
    queryset = ClientPortfolio.objects.all()
    permission_classes = [AllowAny]
