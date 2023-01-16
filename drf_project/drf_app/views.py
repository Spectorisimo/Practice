from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .serializer import AccountSerializer, WalletSerializer
from .filters import WalletFilter
from .services import AccountServicesV1, WalletServicesV1


class WalletAPI(ModelViewSet):
    wallet_services = WalletServicesV1()
    serializer_class = WalletSerializer
    queryset = wallet_services.get_wallets()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = WalletFilter


class AccountAPI(ModelViewSet):
    account_services = AccountServicesV1()
    serializer_class = AccountSerializer
    queryset = account_services.get_accounts()
