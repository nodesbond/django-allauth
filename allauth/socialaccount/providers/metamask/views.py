from allauth.socialaccount.providers.base.views import WalletLoginView

from .provider import MetamaskProvider


class MetamaskLoginView(WalletLoginView):
    provider_id = MetamaskProvider.id


login_with_wallet = MetamaskLoginView.as_view()
