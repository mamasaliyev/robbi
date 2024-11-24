# register/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import RegisterView, VerifyEmailView, LoginView, LogoutView, LanguageListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('languages/', LanguageListView.as_view(), name='language-list'),
]

if settings.DEBUG:  # Faqat DEBUG rejimida ishlaydi
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)