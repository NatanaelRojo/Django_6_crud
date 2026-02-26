from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    # Admin route
    path("admin/", admin.site.urls),
    # Include the built-in auth URLs for login/logout/password management.
    path("accounts/", include("django.contrib.auth.urls")),
    path(
        "logged-out",
        TemplateView.as_view(template_name="registration/logged_out.html"),
        name="logged_out",
    ),
    path("", TemplateView.as_view(template_name="users/index.html"), name="home"),
    # Include the URLs from person app.
    # path("", include("apps.person.urls")),
    # Include the URLs from product app.
    path("products/", include("apps.product.urls")),
    path("users/", include("apps.users.urls")),
]
