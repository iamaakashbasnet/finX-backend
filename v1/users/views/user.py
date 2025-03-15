from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from ..serializers.user import UserSerializer
from ..utils.send_account_creation_email import send_account_verification_email
from ..utils.username_generator import generate_unique_username


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

        if user_exists:
            return Response({'detail': user_exists}, status=HTTP_200_OK)
        else:
            return Response({'detail': user_exists}, status=HTTP_400_BAD_REQUEST)


class CreateUserWithEmailOnlyView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user_email = request.data.get('email')
        if not user_email:
            return Response({'error': 'Email is required'}, status=HTTP_400_BAD_REQUEST)

        try:
            user = get_user_model().objects.create(email=user_email, username=generate_unique_username(user_email))
            toke_generator = PasswordResetTokenGenerator()
            token = toke_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            send_account_verification_email(request, user, token, uid)
            return Response({'detail': 'User created successfully'}, status=HTTP_200_OK)
        except:
            return Response({'error': 'Unable to create user'}, status=HTTP_400_BAD_REQUEST)
