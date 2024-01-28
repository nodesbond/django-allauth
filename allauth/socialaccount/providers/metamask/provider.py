import random
import string

from allauth.socialaccount import app_settings as allauth_app_settings

from allauth.socialaccount.providers.base import (
    Provider,
    ProviderAccount,
    ProviderException,
)
from eth_account.messages import encode_defunct
from web3 import Web3


class MetamaskAccount(ProviderAccount):
    def to_str(self):
        return self.account.uid


class MetamaskProvider(Provider):
    id = "metamask"
    name = "Metamask"
    account_class = MetamaskAccount

    @property
    def get_app_settings(self) -> dict:
        return allauth_app_settings.PROVIDERS.get(self.id, {})

    @staticmethod
    def get_nonce() -> str:
        return "".join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            for _ in range(32)
        )

    def verify_signature(self, account: str, social_token: str, nonce: str) -> bool:
        w3 = Web3(Web3.HTTPProvider(self.get_app_settings.get("url")))
        message_hash = encode_defunct(text=social_token)
        recovered_account_address = w3.eth.account.recover_message(
            message_hash, signature=nonce
        )
        return bool(recovered_account_address.upper() == account.upper())

    def extract_common_fields(self, data) -> dict:
        return dict(
            username=data.get("account"),
        )

    def extract_uid(self, data) -> str:
        if "account" not in data:
            raise ProviderException("metamask error", data)
        return str(data["account"])


provider_classes = [MetamaskProvider]
