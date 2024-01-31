from allauth.socialaccount.providers.keplr.provider import KeplrProvider
from allauth.tests import TestCase, patch


class KeplrTests(TestCase):
    provider_id = KeplrProvider.id
