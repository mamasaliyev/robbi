from django.db import models


class clinic(models.Model):
    title = models.CharField(max_length=100)
    jop_time = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.title
class clinic_and_sanatorium(models.Model):
    GOLD = 'Gold'
    SILVER = 'Silver'
    STANDARD = 'Standard'

    TIER_CHOICES = [
        (GOLD, 'Gold'),
        (SILVER, 'Silver'),
        (STANDARD, 'Standard'),
    ]

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hotels/', null=True, blank=True)
    jop_time = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    tier = models.CharField(
        max_length=10,
        choices=TIER_CHOICES,
        default=STANDARD,
    )

    def __str__(self):
        return f"{self.title} ({self.tier})"