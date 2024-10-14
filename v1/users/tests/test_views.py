from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TokenTests(APITestCase):
    def setUp(self):
        """Create a user for testing."""
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'password123'
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_token_obtain(self):
        """Test obtaining a token."""
        response = self.client.post(reverse('token-obtain'), {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('at', response.data)  # Access token
        self.assertIn('rt', response.cookies)  # Refresh token cookie

    def test_token_refresh(self):
        """Test refreshing a token."""
        # First obtain a token
        response = self.client.post(reverse('token-obtain'), {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        # Get the refresh token from cookies
        refresh_token = response.cookies['rt'].value

        # Now refresh the token
        # Set the refresh token cookie
        self.client.cookies['rt'] = refresh_token
        response = self.client.post(reverse('token-refresh'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('at', response.data)  # New access token

    def test_token_verify(self):
        """Test verifying a token."""
        # Obtain a token
        response = self.client.post(reverse('token-obtain'), {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        access_token = response.data['at']

        # Now verify the token
        response = self.client.post(
            reverse('token-verify'), {'token': access_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token_blacklist(self):
        """Test blacklisting a token."""
        # Obtain a token
        response = self.client.post(reverse('token-obtain'), {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        refresh_token = response.cookies['rt'].value  # Get the refresh token

        # Now blacklist the token
        # Set the refresh token cookie
        self.client.cookies['rt'] = refresh_token
        response = self.client.post(reverse('token-blacklist'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Try to refresh the token again (should fail)
        response = self.client.post(reverse('token-refresh'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
