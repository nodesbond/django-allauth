from allauth.socialaccount.providers.base.views import WalletLoginView

from .provider import WalletconnectProvider


class WalletconnectLoginView(WalletLoginView):
    provider_id = WalletconnectProvider.id


login_with_wallet = WalletconnectLoginView.as_view()
