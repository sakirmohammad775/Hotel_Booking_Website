from django.conf import settings
from django.db import models
from cloudinary.models import CloudinaryField

User = settings.AUTH_USER_MODEL


class Hotel(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available_rooms = models.PositiveIntegerField()
    image = CloudinaryField('hotels')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["hotel", "user"]  # one review per user

    def __str__(self):
        return f"{self.hotel} - {self.rating}"