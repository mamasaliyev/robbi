from rest_framework import serializers
from .models import CustomUser, Language


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name', 'code']


class RegisterSerializer(serializers.ModelSerializer):
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'language']

    def create(self, validated_data):
        language = validated_data.pop('language', None)
        user = CustomUser.objects.create_user(**validated_data)
        user.language = language
        user.is_active = False  # Tasdiqlanishgacha foydalanuvchi faol emas
        user.save()
        return user


class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    verification_code = serializers.CharField(max_length=6)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()  # Faqat email so'raladi, parol kerak emas
