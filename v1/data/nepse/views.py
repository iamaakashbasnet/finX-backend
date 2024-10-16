from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from v1.data.nepse.services.nepse_api import NepseAPI


class LiveMarketView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response(NepseAPI.get_live_market())


class NepseIndexView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response(NepseAPI.get_nepse_index())


class NepseSubIndicesView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response(NepseAPI.get_nepse_sub_indices())
