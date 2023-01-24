from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .serializer import AccountSerializer, WalletSerializer, CreateAccountSerializer, RetrieveAccountSerializer
from .filters import WalletFilter
from .services import AccountServicesV1, WalletServicesV1
from .pagination import CustomPageNumberPagination,CustomCursorPagination


class WalletAPI(ModelViewSet):
    wallet_services = WalletServicesV1()
    serializer_class = WalletSerializer
    queryset = wallet_services.get_wallets()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = WalletFilter


class AccountAPI(ModelViewSet):
    account_services = AccountServicesV1()
    serializer_class = AccountSerializer
    pagination_class = CustomCursorPagination
    def get_queryset(self):
        return self.account_services.get_accounts(action=self.action)

    # def perform_create(self, serializer:AccountSerializer):
    #     self.account_services.create_account(data=serializer.validated_data)


class AccountAPIV2(ModelViewSet):
    account_services = AccountServicesV1()
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return RetrieveAccountSerializer
        return CreateAccountSerializer

    def get_queryset(self):
        return self.account_services.get_accounts(action=self.action)

    def perform_create(self, serializer: AccountSerializer):
        self.account_services.create_account(data=serializer.validated_data)
