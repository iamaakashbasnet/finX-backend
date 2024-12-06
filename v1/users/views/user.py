from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from ..serializers.user import UserSerializer


class RequestUserView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
