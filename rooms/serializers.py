from rest_framework import serializers
from .models import Room
from hotels.serializers import HotelSerializer


class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)

    class Meta:
        model = Room
        fields = [
            "id", "hotel", "room_number", "room_type",
            "price_per_night", "capacity", "is_available",
            "description", "image", "created_at"
        ]
        read_only_fields = ["created_at"]