from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model


class UserModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            first_name='Test',
            last_name='User',
            password='password123'
        )

    def test_user_creation(self):
        """Test user is created successfully."""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertTrue(self.user.check_password('password123'))
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertEqual(str(self.user), 'testuser')

    def test_full_name(self):
        """Test the get_full_name method."""
        self.assertEqual(self.user.get_full_name(), 'Test User')

    def test_short_name(self):
        """Test the get_short_name method."""
        self.assertEqual(self.user.get_short_name(), 'Test')

    def test_user_string_representation(self):
        """Test the string representation of the user."""
        self.assertEqual(str(self.user), 'testuser')

    def test_email_normalization(self):
        """Test that email normalization works correctly."""
        user_with_uppercase_email = get_user_model().objects.create_user(
            username='upperemailuser',
            email='UPPERCASE@Example.COM',
            first_name='Upper',
            last_name='Email',
            password='password123'
        )
        self.assertEqual(user_with_uppercase_email.email,
                         'uppercase@example.com')

    def test_user_date_joined(self):
        """Test that date_joined is set correctly."""
        now = timezone.now()
        self.assertLessEqual(self.user.date_joined, now)

    def test_required_fields(self):
        """Test that user creation requires the right fields."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(username='newuser')

    def test_duplicate_username(self):
        """Test that creating a user with a duplicate username raises an error."""
        with self.assertRaises(Exception):
            get_user_model().objects.create_user(
                username='testuser',
                email='newemail@example.com',
                first_name='New',
                last_name='User',
                password='password123'
            )
