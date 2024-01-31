from allauth.socialaccount.providers.base.views import WalletLoginView

from .provider import KeplrProvider


class KeplrLoginView(WalletLoginView):
    provider_id = KeplrProvider.id


login_with_wallet = KeplrLoginView.as_view()
