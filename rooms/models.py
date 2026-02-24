from django.db import models
from django.conf import settings
from hotels.models import Hotel
from cloudinary.models import CloudinaryField

User = settings.AUTH_USER_MODEL  # Optional if you want to connect Room with User later

class Room(models.Model):

    ROOM_TYPE = (
        ("single", "Single"),
        ("double", "Double"),
        ("suite", "Suite"),
    )

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    room_number = models.CharField(max_length=20)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('rooms')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["hotel", "room_number"]

    def __str__(self):
        return f"{self.hotel.name} - Room {self.room_number}"