from rest_framework.serializers import ModelSerializer

from ..models import PoolInvestmentPortfolio, ClientPortfolio


class PoolInvestmentPortfolioSerializer(ModelSerializer):
    class Meta:
        model = PoolInvestmentPortfolio
        fields = ['name']


class ClientPortfolioSerializer(ModelSerializer):
    class Meta:
        model = ClientPortfolio
        fields = ['client']
