from rest_framework.routers import DefaultRouter
from drf_app.views import AccountAPI, WalletAPI
# Ссылается на версии представлений внутри своего приложения
router = DefaultRouter()
router.register(r'accounts', AccountAPI,basename='accounts-v1')
router.register(r'wallets', WalletAPI)
urlpatterns = router.urls
