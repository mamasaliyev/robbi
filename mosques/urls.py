from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MosquesViewSet, MosquesInfoViewSet

router = DefaultRouter()
router.register(r'mosques', MosquesViewSet)
router.register(r'mosques-info', MosquesInfoViewSet)

urlpatterns = [
    path('Mosques/', include(router.urls)),
]
