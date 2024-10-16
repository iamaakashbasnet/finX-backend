from django.test import TestCase
from django.utils import timezone

from v1.data.nepse.models import Security, SecurityData


class SecurityModelTest(TestCase):
    """
    Tests for the Security model.
    """

    def setUp(self):
        self.security = Security.objects.create(symbol="NABIL", security_name="Nabil Bank")

    def test_security_creation(self):
        self.assertEqual(self.security.symbol, "NABIL")
        self.assertEqual(self.security.security_name, "Nabil Bank")

    def test_security_string_representation(self):
        self.assertEqual(str(self.security), "Nabil Bank")


class SecurityDataModelTest(TestCase):
    """
    Tests for the SecurityData model.
    """

    def setUp(self):
        self.security = Security.objects.create(symbol="NABIL", security_name="Nabil Bank")
        self.security_data = SecurityData.objects.create(
            security=self.security,
            last_traded_price=800.00,
            open_price=790.00,
            high_price=810.00,
            low_price=780.00,
            previous_close=795.00,
            last_updated_datetime=timezone.now()
        )

    def test_security_data_creation(self):
        self.assertEqual(self.security_data.security, self.security)
        self.assertEqual(self.security_data.last_traded_price, 800.00)
        self.assertEqual(self.security_data.open_price, 790.00)
        self.assertEqual(self.security_data.high_price, 810.00)
        self.assertEqual(self.security_data.low_price, 780.00)
        self.assertEqual(self.security_data.previous_close, 795.00)

    def test_security_data_string_representation(self):
        self.assertEqual(str(self.security_data), "Nabil Bank")
