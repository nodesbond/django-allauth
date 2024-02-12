from django.urls import path

from . import views

urlpatterns = [
    path(
        "walletconnect/login/",
        views.login_with_wallet,
        name="walletconnect_login",
    ),
]
