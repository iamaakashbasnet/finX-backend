from django.db import models
from django.utils.translation import gettext_lazy as _


class Security(models.Model):
    """
    Represents a security (e.g., stock) traded on the Nepal Stock Exchange.

    Attributes:
        symbol (str): A unique symbol identifying the security.
        security_name (str): The full name of the security.
    """
    symbol = models.CharField(_('symbol'), max_length=100, unique=True)
    security_name = models.CharField(_('security name'), max_length=100)

    class Meta:
        ordering = ['security_name']
        verbose_name = _("Security")
        verbose_name_plural = _("Securities")

    def __str__(self):
        return f"{self.security_name}"


class SecurityData(models.Model):
    """
    Stores trading data for a specific security, linked via a one-to-one relationship.

    Attributes:
        security (Security): The related security for which this trading data is recorded.
        last_traded_price (Decimal): The most recent trading price of the security.
        open_price (Decimal): The price of the security when the market opened.
        high_price (Decimal): The highest price of the security during the trading session.
        low_price (Decimal): The lowest price of the security during the trading session.
        previous_close (Decimal): The closing price of the security from the previous session.
        last_updated_datetime (DateTime): The last time this data was updated.
    """
    security = models.OneToOneField(Security, on_delete=models.CASCADE, verbose_name=_('security'))
    last_traded_price = models.DecimalField(_('last traded price'), default=0.00, max_digits=10, decimal_places=2)
    open_price = models.DecimalField(_('open price'), default=0.00, max_digits=10, decimal_places=2)
    high_price = models.DecimalField(_('high price'), default=0.00, max_digits=10, decimal_places=2)
    low_price = models.DecimalField(_('low price'), default=0.00, max_digits=10, decimal_places=2)
    previous_close = models.DecimalField(_('previous close'), default=0.00, max_digits=10, decimal_places=2)
    last_updated_datetime = models.DateTimeField(_('last updated datetime'), null=True, blank=True, default=None)

    class Meta:
        ordering = ['security']
        verbose_name = _("Security Data")
        verbose_name_plural = _("Security Datas")

    def __str__(self):
        return f"{self.security.security_name}"
