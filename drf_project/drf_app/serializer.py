from rest_framework import serializers
from .models import Account, Wallet


class _WalletAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name')


class WalletSerializer(serializers.ModelSerializer):
    account = _WalletAccountSerializer(read_only=True)

    class Meta:
        model = Wallet
        fields = '__all__'


class _AccountWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('amount', 'currency')


class AccountSerializer(serializers.ModelSerializer):
    # wallets = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    wallets = _AccountWalletSerializer(read_only=True, many=True)
    total = serializers.DecimalField(max_digits=14,decimal_places=2)
    class Meta:
        model = Account
        fields = '__all__'
