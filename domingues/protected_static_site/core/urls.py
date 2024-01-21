from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path(
        "accounts/",
        include(
            [
                path(
                    "login",
                    auth_views.LoginView.as_view(
                        template_name="protected_static_site/login.html"
                    ),
                    name="login",
                ),
                path("profile", views.Profile.as_view(), name="profile"),
                path("logout", auth_views.LogoutView.as_view(), name="logout"),
            ]
        ),
    ),
    path(
        "",
        views.ServeStaticSite.as_view(),
    ),
    path(
        "<path:path>",
        views.ServeStaticSite.as_view(),
    ),
]
