from rest_framework.serializers import ModelSerializer

from v1.data.nepse.serializers import SecuritySerializer
from ..models import PoolInvestmentPortfolioEntry, ClientPortfolioEntry


class PoolInvestmentPortfolioEntrySerializer(ModelSerializer):
    security = SecuritySerializer()

    class Meta:
        model = PoolInvestmentPortfolioEntry
        fields = ['portfolio', 'security', 'type', 'quantity', 'remaining_quantity', 'rate', 'total_investment',
                  'created_at']


class ClientPortfolioEntrySerializer(ModelSerializer):
    security = SecuritySerializer()
    
    class Meta:
        model = ClientPortfolioEntry
        fields = ['portfolio', 'security', 'type', 'quantity', 'remaining_quantity', 'rate', 'total_investment',
                  'created_at']
