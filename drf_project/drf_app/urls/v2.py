from rest_framework import routers

from drf_app.views import AccountAPI, WalletAPI, AccountAPIV2

router = routers.DefaultRouter()
router.register(r'accounts', AccountAPIV2,basename='accounts-v2')
urlpatterns = router.urls
