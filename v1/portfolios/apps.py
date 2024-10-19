from django.apps import AppConfig


class PortfoliosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "v1.portfolios"

    def ready(self):
        import v1.portfolios.signals
