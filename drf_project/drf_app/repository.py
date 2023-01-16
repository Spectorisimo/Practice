from typing import Protocol
from django.db.models import QuerySet, Sum, Avg, Case, When, Q, F, DecimalField
from .constants import WalletCurrencyTypes

from .models import Account, Wallet


class AccountRepositoryInterface(Protocol):
    @staticmethod
    def get_accounts() -> QuerySet[Account]: ...


class WalletRepositoryInterface(Protocol):
    @staticmethod
    def get_wallets() -> QuerySet[Wallet]: ...


class AccountRepositoryV1:
    @staticmethod
    def get_accounts() -> QuerySet[Account]:
        return Account.objects.prefetch_related('wallets').annotate(
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


class WalletRepositoryV1:
    @staticmethod
    def get_wallets() -> QuerySet[Wallet]:
        return Wallet.objects.select_related('account')
