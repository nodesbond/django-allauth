from allauth.socialaccount.providers.base import CryptoWalletProvider


class TrustWalletProvider(CryptoWalletProvider):
    id = "trustwallet"
    name = "Trust"


provider_classes = [TrustWalletProvider]
