from typing import NamedTuple

from django.db import models
from .constants import WalletCurrencyTypes


# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Wallet(models.Model):
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE, related_name='wallets')
    amount = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=3, choices=WalletCurrencyTypes.choices, default=WalletCurrencyTypes.KZT)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
