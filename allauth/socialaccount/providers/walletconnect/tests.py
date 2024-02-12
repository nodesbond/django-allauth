from allauth.socialaccount.providers.walletconnect.provider import WalletconnectProvider
from allauth.tests import TestCase


class WalletconnectTests(TestCase):
    provider_id = WalletconnectProvider.id
