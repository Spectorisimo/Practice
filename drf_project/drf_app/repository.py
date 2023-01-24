from typing import Protocol, OrderedDict
from django.db.models import QuerySet, Sum, Case, When, Q, F, DecimalField
from .constants import WalletCurrencyTypes
from django.db import transaction
from .models import Account, Wallet


class AccountRepositoryInterface(Protocol):
    @staticmethod
    def get_accounts(action: str) -> QuerySet[Account]: ...

    @staticmethod
    def create_account(data: OrderedDict) -> None: ...


class WalletRepositoryInterface(Protocol):
    @staticmethod
    def get_wallets() -> QuerySet[Wallet]: ...


class AccountRepositoryV1:

    @staticmethod
    def get_accounts(action: str) -> QuerySet[Account]:
        accounts = Account.objects.all()
        if action not in ('list', 'retrieve'):
            return accounts

        return accounts.prefetch_related('wallets').annotate(
            total=Sum(
                Case(
                    When(Q(wallets__currency=WalletCurrencyTypes.RUB), then=F('wallets__amount') * 6.7),
                    When(Q(wallets__currency=WalletCurrencyTypes.EUR), then=F('wallets__amount') * 501),
                    When(Q(wallets__currency=WalletCurrencyTypes.USD), then=F('wallets__amount') * 467),
                    When(Q(wallets__currency=WalletCurrencyTypes.KZT), then=F('wallets__amount') * 1),
                    output_field=DecimalField(),
                    default=0.00,
                )
            )

        )

    @staticmethod
    @transaction.atomic()  # в случае ошибки функции, любые изменения в базе данных не применятся - ROLLBACK
    def create_account(data: OrderedDict) -> None:
        wallets = data.pop('wallets')
        account = Account.objects.create(**data)
        Wallet.objects.bulk_create([
            Wallet(**w, account=account) for w in wallets
        ])


class WalletRepositoryV1:
    @staticmethod
    def get_wallets() -> QuerySet[Wallet]:
        return Wallet.objects.select_related('account')
