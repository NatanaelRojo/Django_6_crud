from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.users.forms import CustomUserChangeForm, CustomUserCreationForm


class UserListView(ListView):
    model = get_user_model()
    template_name = "users/user_list.html"
    context_object_name = "users"


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = "users/user_detail.html"
    context_object_name = "user"


class UserCreateView(CreateView):
    model = get_user_model()
    template_name = "users/user_form.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:user_list")


class UserUpdateView(UpdateView):
    model = get_user_model()
    template_name = "users/user_form.html"
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("users:user_list")


class UserDeleteView(DeleteView):
    model = get_user_model()
    template_name = "users/user_confirm_delete.html"
    success_url = reverse_lazy("users:user_list")
