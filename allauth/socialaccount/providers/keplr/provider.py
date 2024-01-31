from allauth.socialaccount.providers.base import CryptoWalletProvider


class KeplrProvider(CryptoWalletProvider):
    id = "keplr"
    name = "Keplr"


provider_classes = [KeplrProvider]
