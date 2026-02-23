from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Booking
from . import serializers as bookingSz
from .services import BookingService


class BookingViewSet(ModelViewSet):

    http_method_names = ["get", "post", "patch", "delete"]

    @action(detail=True, methods=["post"])
    def cancel(self, request, pk=None):
        booking = self.get_object()
        BookingService.cancel_booking(booking=booking, user=request.user)
        return Response({"status": "Booking canceled"})

    def get_permissions(self):
        if self.action in ["destroy"]:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == "cancel":
            return bookingSz.EmptySerializer
        if self.action == "create":
            return bookingSz.CreateBookingSerializer
        elif self.action == "partial_update":
            return bookingSz.UpdateBookingSerializer
        return bookingSz.BookingSerializer

    def get_serializer_context(self):
        return {"user": self.request.user}

    def get_queryset(self):
        if self.request.user.is_staff:
            return Booking.objects.select_related("room", "user").all()

        return Booking.objects.select_related("room", "user").filter(
            user=self.request.user
        )