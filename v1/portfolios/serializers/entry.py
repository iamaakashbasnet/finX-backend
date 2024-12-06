from rest_framework.serializers import ModelSerializer

from ..models import PoolInvestmentPortfolioEntry, ClientPortfolioEntry


class PoolInvestmentPortfolioEntrySerializer(ModelSerializer):
    class Meta:
        model = PoolInvestmentPortfolioEntry
        fields = ['portfolio', 'security', 'quantity', 'rate', 'total_investment', 'current_value', 'created_at']


class ClientPortfolioEntrySerializer(ModelSerializer):
    class Meta:
        model = ClientPortfolioEntry
        fields = ['portfolio', 'security', 'quantity', 'rate', 'total_investment', 'current_value', 'created_at']
