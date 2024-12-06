from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger konfiguratsiyasi
schema_view = get_schema_view(
    openapi.Info(
        title="Robbi API Hujjatlari",
        default_version='v1',
        description="6 ta app uchun API hujjatlari",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panelga yo‘l
    # API URL'lar
    path('registers/', include('registers.urls')),  # registers app
    path('clinic_and_sanatorium/', include('clinic_and_sanatorium.urls')),  # clinic_and_sanatorium app
    path('hotels/', include('hotels.urls')),  # hotels app
    path('restaruants/', include('restaruants.urls')),  # restaurants app
    path('parks/', include('parks.urls')),  # parks app
    path('mosques/', include('mosques.urls')),  # mosques app

    # Swagger hujjatlari
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
