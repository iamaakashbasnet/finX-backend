from django.contrib.auth import get_user_model
from django.db import models


class Firm(models.Model):
    """
    Represents a firm within the system, containing managers and clients.

    Fields:
    - name: The name of the firm.
    - managers: A ManyToMany relationship to the User model, representing users who manage this firm.
      The reverse relation (from User to Firm) can be accessed using 'managed_firms'.
    - clients: A ManyToMany relationship to the User model, representing users who are clients of this firm.
      The reverse relation (from User to Firm) can be accessed using 'client_firms'.

    Methods:
    - __str__: Returns the string representation of the firm, which is its name.
    """
    name = models.CharField(max_length=255)
    managers = models.ManyToManyField(get_user_model(), related_name='managed_firms', blank=True)

    def __str__(self):
        return self.name
