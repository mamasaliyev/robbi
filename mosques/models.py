from django.core.validators import RegexValidator
from django.db import models


class Mosques(models.Model):
    title = models.CharField(max_length=100)  # Masjid nomi
    jop_time = models.CharField(max_length=50)  # Ish vaqti
    image = models.ImageField(upload_to='images/')  # Rasmlar uchun
    address = models.CharField(max_length=255)  # Manzil
    latitude = models.FloatField(null=True, blank=True)  # Kenglik
    longitude = models.FloatField(null=True, blank=True)  # Uzunlik
    tel = models.CharField(  # Telefon raqami
        max_length=20,
        null=True,
        blank=True,
        validators=[RegexValidator(
            regex=r'^\+?[0-9\s\-\(\)]{9,20}$',
            message="Telefon raqami: +998901234567 formatida bo‘lishi kerak."
        )]
    )

    def __str__(self):
        return self.title


class PrayerTimes(models.Model):
    mosque = models.ForeignKey(Mosques, on_delete=models.CASCADE, related_name='prayer_times')
    bomdod = models.TimeField()  # Bomdod
    quyosh = models.TimeField()  # Quyosh chiqishi
    peshin = models.TimeField()  # Peshin
    asr = models.TimeField()  # Asr
    shom = models.TimeField()  # Shom
    xufton = models.TimeField()  # Xufton
    date = models.DateField(auto_now_add=True)  # Sana (qaysi kun uchun)

    class Meta:
        unique_together = ('mosque', 'date')  # Har bir kun uchun masjidga tegishli vaqtlar

    def __str__(self):
        return f"{self.mosque.title} - {self.date}"



