from rest_framework import serializers

from .models import Security, SecurityData


class SecuritySerializer(serializers.ModelSerializer):
    """
    Serializer for the Security model.
    """

    class Meta:
        model = Security
        fields = ['id', 'symbol', 'security_name']


class SecurityDataSerializer(serializers.ModelSerializer):
    """
    Serializer for the SecurityData model, including the related Security data.
    """
    security = SecuritySerializer()

    class Meta:
        model = SecurityData
        fields = ['id', 'security', 'last_traded_price', 'open_price', 'high_price',
                  'low_price', 'previous_close', 'last_updated_datetime']
