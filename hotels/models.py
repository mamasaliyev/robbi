from django.db import models
from django.core.validators import RegexValidator

class Hotels(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hotels/', null=True, blank=True)
    job_time = models.CharField(max_length=50)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Hotel_information(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hotels/', null=True, blank=True)
    job_time = models.CharField(max_length=50)
    tel = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[RegexValidator(
            regex=r'^\+?[0-9\s\-\(\)]{9,20}$',
            message="Enter a valid phone number. Allowed formats: +1234567890, +1 234 567 890, etc."
        )]
    )
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    # Add a field for the star rating
    STAR_RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    star_rating = models.IntegerField(choices=STAR_RATING_CHOICES)

    def __str__(self):
        return self.title