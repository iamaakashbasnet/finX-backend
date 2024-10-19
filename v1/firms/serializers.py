from rest_framework import serializers

from .models import Firm


class FirmSerializer(serializers.ModelSerializer):
    managers_count = serializers.SerializerMethodField()
    clients_count = serializers.SerializerMethodField()

    class Meta:
        model = Firm
        fields = ['id', 'name', 'managers_count', 'clients_count']

    def get_managers_count(self, obj):
        return obj.managers.count()

    def get_clients_count(self, obj):
        return obj.clients.count()
