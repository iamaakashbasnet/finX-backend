from django.db.models import Sum, F, Q
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from v1.data.nepse.serializers import SecuritySerializer
from v1.data.nepse.models import Security
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


class EntrySummaryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        entries = PoolInvestmentPortfolioEntry.objects.filter(portfolio=kwargs.get('portfolio_pk'))

        summary = (
            entries.values('security')  # Group by security
            .annotate(
                net_total_shares=Sum('remaining_quantity'),
                total_cost=Sum(F('quantity') * F('rate'), filter=Q(type='BUY')),
                total_bought_shares=Sum('quantity', filter=Q(type='BUY'))
            )
            .values('security', 'net_total_shares', 'total_cost', 'total_bought_shares')
        )

        result = []
        for entry in summary:
            security = entry['security']
            net_total_shares = entry['net_total_shares'] or 0
            total_cost = entry['total_cost'] or 0
            total_bought_shares = entry['total_bought_shares'] or 0

            # Calculate average cost
            average_cost = total_cost / total_bought_shares if total_bought_shares > 0 else 0

            result.append({
                "security": SecuritySerializer(Security.objects.get(pk=security)).data,
                "quantity": net_total_shares,
                "rate": round(average_cost, 2),
            })

        return Response(result)
