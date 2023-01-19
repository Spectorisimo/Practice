from django.urls import path, include

urlpatterns = [
    path('', include('drf_app.urls.v2')),
]
