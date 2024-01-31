from django.urls import path

from . import views

urlpatterns = [
    path(
        "keplr/login/",
        views.login_with_wallet,
        name="keplr_login",
    ),
]
