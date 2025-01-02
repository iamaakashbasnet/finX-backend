from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from ..serializers.user import UserSerializer


class RequestUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class UserWithEmailCheckView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response({'error': 'Email is required'}, status=HTTP_400_BAD_REQUEST)

        try:
            validate_email(email)
        except ValidationError:
            return Response({'error': 'Invalid email format'}, status=HTTP_400_BAD_REQUEST)

        user_exists = get_user_model().objects.filter(email=email).exists()
        return Response({'detail': user_exists}, status=HTTP_200_OK)
