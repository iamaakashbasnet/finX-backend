from django.db import models


class FundDetail(models.Model):
    cash_at_bank = models.DecimalField(max_digits=15, decimal_places=2, help_text="Cash available in the bank.")
    cash_on_hold = models.DecimalField(max_digits=15, decimal_places=2,
                                       help_text="Cash on hold due to IPO applications.")
    fund_reserve = models.DecimalField(max_digits=15, decimal_places=2, help_text="Reserve funds.")


class CapitalDetail(models.Model):
    paid_up_capital = models.DecimalField(max_digits=15, decimal_places=2, help_text="Total paid-up capital.")
    total_share_units = models.PositiveIntegerField(help_text="Total number of share units.")
    nav_value = models.DecimalField(max_digits=10, decimal_places=2)

class ProfitDetail(models.Model):
    unreleased_profit = models.DecimalField(max_digits=15, decimal_places=2,
                                            help_text="Profit that is not yet realized.")
    distributable_profit = models.DecimalField(max_digits=15, decimal_places=2,
                                               help_text="Profit available for distribution.")
    operational_cost = models.DecimalField(max_digits=15, decimal_places=2,
                                           help_text="Operational cost.")
