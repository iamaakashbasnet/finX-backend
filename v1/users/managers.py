from django.apps import apps
from django.contrib.auth.models import BaseUserManager
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """Create and return a user with an email, username, and password."""
        if not username:
            raise ValueError(_("The given username must be set"))
        if email is None:
            raise ValueError(_("The given email must be set"))

        email = self.normalize_email(email).lower()

        # Lookup the real model class from the global app registry
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)

        # Create user instance
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        """Create a regular user."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """Create and return a superuser."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError(_("Superuser must have is_staff=True."))
        if not extra_fields.get("is_superuser"):
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self._create_user(username, email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        """Return a queryset of users with a specific permission."""
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    _("You have multiple authentication backends configured and "
                      "must provide the `backend` argument.")
                )
        elif not isinstance(backend, str):
            raise TypeError(
                _("Backend must be a dotted import path string (got %r)." % backend))
        else:
            backend = auth.load_backend(backend)

        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()
