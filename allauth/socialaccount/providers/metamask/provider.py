from allauth.socialaccount.providers.base import CryptoWalletProvider


class MetamaskProvider(CryptoWalletProvider):
    id = "metamask"
    name = "Metamask"


provider_classes = [MetamaskProvider]
