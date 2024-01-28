from allauth.socialaccount.providers.metamask.provider import MetamaskProvider
from django.test.utils import override_settings
from django.urls import reverse

from allauth.tests import TestCase, patch
from allauth.utils import get_user_model


class MetamaskTests(TestCase):
    provider_id = MetamaskProvider.id
