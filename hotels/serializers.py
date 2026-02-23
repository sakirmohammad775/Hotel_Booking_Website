from rest_framework import serializers
from .models import Hotel, Review
from users.serializers import UserSerializer


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ["id", "name", "description", "location", "price_per_night", "available_rooms", "image", "created_at"]
        read_only_fields = ["created_at"]


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "hotel", "user", "rating", "comment", "created_at"]
        read_only_fields = ["user", "created_at"]