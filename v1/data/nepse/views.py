from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from v1.data.nepse.models import SecurityData, Security
from v1.data.nepse.serializers import SecurityDataSerializer, SecuritySerializer
from v1.data.nepse.services.nepse_api import NepseAPI


class UpdateDataView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        NepseAPI.update_data()
        return Response({"result": "true"})


class ListedSecuritiesView(ListAPIView):
    serializer_class = SecuritySerializer
    permission_classes = (AllowAny,)
    queryset = Security.objects.all()


class ListedSecuritiesDataView(ListAPIView):
    serializer_class = SecurityDataSerializer
    permission_classes = (AllowAny,)
    queryset = SecurityData.objects.all()


class NepseIndexView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response(NepseAPI.get_nepse_index())


class NepseSubIndicesView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response(NepseAPI.get_nepse_sub_indices())
