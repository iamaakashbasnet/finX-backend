from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Firm
from .serializers import FirmSerializer


class FirmCreateView(generics.CreateAPIView):
    """
    View for creating a new firm by setting requesting user as manager
    """
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        firm = serializer.save()
        firm.managers.add(self.request.user)


class FirmListView(generics.ListAPIView):
    """
    List all firm of a request user
    """
    serializer_class = FirmSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Firm.objects.filter(managers=self.request.user)
