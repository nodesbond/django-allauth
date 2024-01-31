from django.urls import path

from . import views

urlpatterns = [
    path(
        "trustwallet/login/",
        views.login_with_wallet,
        name="trestwallet_login",
    ),
]
