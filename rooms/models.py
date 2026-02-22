from django.db import models
from hotels.models import Hotel


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
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hotel.name} - {self.room_number}"