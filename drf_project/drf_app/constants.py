from django.db import models


class WalletCurrencyTypes(models.TextChoices):
    RUB = 'RUB'
    EUR = 'EUR'
    USD = 'USD'
    KZT = 'KZT'
