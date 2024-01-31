from allauth.socialaccount.providers.base.views import WalletLoginView

from .provider import TrustWalletProvider


class TrustWalletLoginView(WalletLoginView):
    provider_id = TrustWalletProvider.id


login_with_wallet = TrustWalletLoginView.as_view()
