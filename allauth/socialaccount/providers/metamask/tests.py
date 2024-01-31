from allauth.socialaccount.providers.metamask.provider import MetamaskProvider
from allauth.tests import TestCase


class MetamaskTests(TestCase):
    provider_id = MetamaskProvider.id
