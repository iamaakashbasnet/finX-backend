from rest_framework import serializers

from .models import Firm


class FirmSerializer(serializers.ModelSerializer):
    managers_count = serializers.SerializerMethodField()
    pool_investment_clients_count = serializers.SerializerMethodField()
    general_clients_count = serializers.SerializerMethodField()

    class Meta:
        model = Firm
        fields = ['id', 'name', 'managers_count', 'pool_investment_clients_count', 'general_clients_count']

    def get_managers_count(self, obj):
        return obj.managers.count()

    def get_pool_investment_clients_count(self, obj):
        return obj.poolinvestmentclient_set.count()

    def get_general_clients_count(self, obj):
        return obj.generalclient_set.count()
