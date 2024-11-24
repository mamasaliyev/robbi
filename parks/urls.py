from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParksViewSet, ParksInfoViewSet

router = DefaultRouter()
router.register(r'parks', ParksViewSet)
router.register(r'parks-info', ParksInfoViewSet)

urlpatterns = [
    path('parks/', include(router.urls)),
]
