"""Class-based views for user CRUD operations.

This module exposes a small set of generic class-based views that
operate on the project's custom user model. Each view sets a
`template_name` and, where appropriate, a form class and
`success_url` for redirects after successful operations.

Views:
    - `UserListView`: list all users
    - `UserDetailView`: show a single user's details
    - `UserCreateView`: create a new user (uses `CustomUserCreationForm`)
    - `UserUpdateView`: edit an existing user (uses `CustomUserChangeForm`)
    - `UserDeleteView`: delete a user
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.users.forms import CustomUserChangeForm, CustomUserCreationForm


class UserListView(LoginRequiredMixin, ListView):
    """Display a list of users.

    Renders the `users/user_list.html` template and exposes the
    queryset in the context under the name `users`.
    """

    model = get_user_model()
    template_name = "users/user_list.html"
    context_object_name = "users"


class UserDetailView(LoginRequiredMixin, DetailView):
    """Display detail for a single user.

    Uses `users/user_detail.html` and puts the object in the context
    as `user`.
    """

    model = get_user_model()
    template_name = "users/user_detail.html"
    context_object_name = "user"


class UserCreateView(LoginRequiredMixin, CreateView):
    """Create a new user instance using `CustomUserCreationForm`."""

    model = get_user_model()
    template_name = "users/user_form.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:user_list")


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """Update an existing user using `CustomUserChangeForm`."""

    model = get_user_model()
    template_name = "users/user_form.html"
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("users:user_list")


class UserDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a user and redirect to the user list."""

    model = get_user_model()
    template_name = "users/user_confirm_delete.html"
    success_url = reverse_lazy("users:user_list")

