from rest_framework import serializers
from .models import Booking
from rooms.models import Room
from wallet.models import Wallet
from users.serializers import UserSerializer
from .services import BookingService


class EmptySerializer(serializers.Serializer):
    pass


class SimpleRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "room_number", "room_type", "price_per_night"]


class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    room = SimpleRoomSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = [
            "id", "user", "room",
            "check_in_date", "check_out_date",
            "total_price", "status", "created_at"
        ]
        read_only_fields = ["user", "total_price", "status", "created_at"]


class CreateBookingSerializer(serializers.Serializer):
    room_id = serializers.IntegerField()
    check_in_date = serializers.DateField()
    check_out_date = serializers.DateField()

    def validate_room_id(self, value):
        if not Room.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Room does not exist")
        return value

    def validate(self, data):
        if data["check_out_date"] <= data["check_in_date"]:
            raise serializers.ValidationError("Check-out must be after check-in")
        return data

    def create(self, validated_data):
        user = self.context["user"]
        return BookingService.create_booking(user=user, **validated_data)

    def to_representation(self, instance):
        return BookingSerializer(instance).data


class UpdateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["status"]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["id", "balance"]