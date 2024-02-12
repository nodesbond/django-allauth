from allauth.socialaccount.providers.base import CryptoWalletProvider


class WalletconnectProvider(CryptoWalletProvider):
    id = "walletconnect"
    name = "Walletconnect"


provider_classes = [WalletconnectProvider]
