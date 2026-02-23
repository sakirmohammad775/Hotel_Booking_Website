from django.db import transaction
from rest_framework.exceptions import ValidationError, PermissionDenied
from .models import Booking
from wallet.models import Wallet
from rooms.models import Room
from datetime import date


class BookingService:

    @staticmethod
    def create_booking(user, room_id, check_in, check_out):

        with transaction.atomic():

            room = Room.objects.get(pk=room_id)

            if not room.is_available:
                raise ValidationError("Room not available")

            nights = (check_out - check_in).days
            total_price = nights * room.price_per_night

            booking = Booking.objects.create(
                user=user,
                room=room,
                check_in=check_in,
                check_out=check_out,
                total_price=total_price,
            )

            Wallet.objects.create(
                booking=booking,
                amount=total_price,
                status=Wallet.PENDING
            )

            return booking

    @staticmethod
    def cancel_booking(booking, user):

        if user.is_staff:
            booking.status = Booking.CANCELED
            booking.save()
            return booking

        if booking.user != user:
            raise PermissionDenied("You can only cancel your booking")

        if booking.status == Booking.COMPLETED:
            raise ValidationError("Cannot cancel completed booking")

        booking.status = Booking.CANCELED
        booking.save()
        return booking