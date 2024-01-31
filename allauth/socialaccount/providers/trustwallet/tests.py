from allauth.socialaccount.providers.trustwallet.provider import TrustWalletProvider
from allauth.tests import TestCase


class TrustWalletTests(TestCase):
    provider_id = TrustWalletProvider.id
