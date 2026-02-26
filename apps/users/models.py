"""Custom user model for the `users` app.

This module defines a `User` model that extends Django's
`AbstractUser` to include an optional `role` field. The model keeps
the default authentication behavior while allowing a simple string
role to be stored for each user (e.g. "admin", "manager").
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Application-specific user model.

    Inherits all fields and behavior from Django's `AbstractUser` and
    adds one optional `role` field to capture a user's role within
    the application.
    """

    role = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        """Return the username as the string representation.

        This keeps compatibility with Django expectations for user
        display and logging.
        """

        return self.username
