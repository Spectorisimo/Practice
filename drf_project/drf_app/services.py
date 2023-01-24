from typing import Protocol, OrderedDict
from django.db.models import QuerySet
from .models import Account, Wallet
from . import repository


class AccountServicesInterface(Protocol):
    account_repository_interface: repository.AccountRepositoryInterface

    def get_accounts(self, action: str) -> QuerySet[Account]: ...

    def create_account(self, data: OrderedDict) -> None: ...


class WalletServicesInterface(Protocol):
    wallet_repository_interface: repository.WalletRepositoryInterface

    def get_wallets(self) -> QuerySet[Wallet]: ...


class AccountServicesV1:
    account_repository: repository.AccountRepositoryV1 = repository.AccountRepositoryV1()

    def get_accounts(self, action) -> QuerySet[Account]:
        return self.account_repository.get_accounts(action)

    def create_account(self, data: OrderedDict) -> None:
        self.account_repository.create_account(data=data)


class WalletServicesV1:
    wallet_repository: repository.WalletRepositoryV1 = repository.WalletRepositoryV1()

    def get_wallets(self) -> QuerySet[Wallet]:
        return self.wallet_repository.get_wallets()
