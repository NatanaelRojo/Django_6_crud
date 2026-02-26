"""Forms for creating and updating the custom `User` model.

This module provides two form classes that wrap Django's built-in
user forms and point them at the project's `User` model. They expose
the common user fields plus the application-specific `role` field.
"""

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    """Form used to create new `User` instances.

    Uses Django's `UserCreationForm` behavior but targets the project's
    custom `User` model and exposes `username`, `email`, `first_name`,
    `last_name`, and `role` fields.
    """

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "role")


class CustomUserChangeForm(UserChangeForm):
    """Form used to edit existing `User` instances.

    Wraps Django's `UserChangeForm` for the project's `User` model and
    exposes the same set of editable fields as the creation form.
    """

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "role")
