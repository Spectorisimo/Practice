from django.urls import path, include
# Ссылается на версии приложений
urlpatterns = [
    path('', include('drf_app.urls.v1')),
]
