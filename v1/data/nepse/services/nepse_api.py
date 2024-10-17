from datetime import datetime
from decimal import Decimal

from django.db import transaction
from nepse import Nepse

from v1.data.nepse.models import Security, SecurityData

nepse = Nepse()
nepse.setTLSVerification(False)


class NepseAPI:
    def __init__(self):
        pass

    @staticmethod
    def get_securities_list():
        securities = nepse.getSecurityList()

        with transaction.atomic():
            for sec in securities:
                Security.objects.update_or_create(
                    symbol=sec['symbol'],
                    defaults={'security_name': sec['securityName']}
                )

    @staticmethod
    def get_securities_data():
        live_market_data = nepse.getLiveMarket()

        with transaction.atomic():
            for live_data in live_market_data:
                security, created = Security.objects.get_or_create(symbol=live_data['symbol'])

                SecurityData.objects.update_or_create(
                    security=security,
                    defaults={
                        'last_traded_price': Decimal(live_data['lastTradedPrice']),
                        'open_price': Decimal(live_data['openPrice']),
                        'high_price': Decimal(live_data['highPrice']),
                        'low_price': Decimal(live_data['lowPrice']),
                        'previous_close': Decimal(live_data['previousClose']),
                        'last_updated_datetime': datetime.strptime(live_data['lastUpdatedDateTime'],
                                                                   '%Y-%m-%d %H:%M:%S.%f')
                    }
                )

    @staticmethod
    def update_data():
        """
        Saves securities related data to database
        """
        NepseAPI.get_securities_list()
        NepseAPI.get_securities_data()

    @staticmethod
    def get_nepse_index():
        """
        Data related to main indices like NEPSE, Sensitive, Float...
        """
        return nepse.getNepseIndex()

    @staticmethod
    def get_nepse_sub_indices():
        """
        Data related to sectoral indices
        """
        return nepse.getNepseSubIndices()
