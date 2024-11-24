from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
import random
import string
from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken

from .models import CustomUser, Language
from .serializers import RegisterSerializer, VerifyEmailSerializer, LoginSerializer, LanguageSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Tasdiqlash kodi yaratish
            verification_code = ''.join(random.choices(string.digits, k=6))
            user.verification_code = verification_code
            user.save()

            # Emailga tasdiqlash kodi yuborish
            send_mail(
                'Tasdiqlash kodi',
                f'Sizning tasdiqlash kodingiz: {verification_code}',
                'no-reply@yourdomain.com',
                [user.email],
                fail_silently=False,
            )

            return Response({
                "message": "Ro'yxatdan o'tdingiz. Emailga tasdiqlash kodi yuborildi."
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):
    def post(self, request):
        serializer = VerifyEmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            verification_code = serializer.validated_data['verification_code']

            try:
                user = CustomUser.objects.get(email=email)
                if user.verification_code == verification_code:
                    user.is_email_verified = True
                    user.is_active = True  # Tasdiqlangach faol bo'ladi
                    user.verification_code = None  # Kodni o'chirish
                    user.save()
                    return Response({"message": "Email tasdiqlandi!"}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Tasdiqlash kodi noto'g'ri!"}, status=status.HTTP_400_BAD_REQUEST)
            except CustomUser.DoesNotExist:
                return Response({"message": "Foydalanuvchi topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']

            try:
                user = get_user_model().objects.get(email=email)

                if not user.is_email_verified:
                    # Email tasdiqlash kodi yuborish
                    verification_code = ''.join(random.choices(string.digits, k=6))
                    user.verification_code = verification_code
                    user.save()

                    send_mail(
                        'Tasdiqlash kodi',
                        f'Sizning tasdiqlash kodingiz: {verification_code}',
                        'no-reply@yourdomain.com',
                        [user.email],
                        fail_silently=False,
                    )

                    return Response({
                        "message": "Tasdiqlash kodi emailga yuborildi."
                    }, status=status.HTTP_200_OK)

                # Token yaratish
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token

                return Response({
                    "message": "Email tasdiqlangan va foydalanuvchi tizimga kirgan!",
                    "access_token": str(access_token),
                    "refresh_token": str(refresh)
                }, status=status.HTTP_200_OK)

            except get_user_model().DoesNotExist:
                return Response({
                    "message": "Foydalanuvchi topilmadi."
                }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "message": "Email formati noto'g'ri yoki mavjud emas."
        }, status=status.HTTP_400_BAD_REQUEST)


class LanguageListView(APIView):
    def get(self, request):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)


from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  # Tizimga kirgan foydalanuvchi bo'lishi kerak
    authentication_classes = [JWTAuthentication]  # JWT orqali autentifikatsiya

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response({"message": "Refresh token taqdim etilmagan!"}, status=status.HTTP_400_BAD_REQUEST)

            # Tokenni bekor qilish
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Foydalanuvchi tizimdan chiqdi."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"Xatolik yuz berdi: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
