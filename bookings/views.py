from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Booking
from . import serializers as bookingSz
from .services import BookingService
from rest_framework.decorators import api_view
from rest_framework import status
from sslcommerz_lib import SSLCOMMERZ
from django.conf import settings as main_settings
from django.shortcuts import redirect

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
        
       
       
@api_view(['POST'])
def initiate_payment(request):
    user = request.user
    amount = request.data.get("amount")
    booking_id = request.data.get("bookingId")
    if not amount or not booking_id:
        return Response({"error": "Amount and Booking ID are required"}, status=status.HTTP_400_BAD_REQUEST)

    settings = {'store_id': 'phima69a67724da275',
                'store_pass': 'phima69a67724da275@ssl', 'issandbox': True}
    
    sslcz = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = amount
    post_body['currency'] = "BDT"
    post_body['tran_id'] = f"txn_{booking_id}"
    post_body['success_url'] = f"{main_settings.BACKEND_URL}/api/v1/payment/success/"
    post_body['fail_url'] = f"{main_settings.BACKEND_URL}/api/v1/payment/fail/"
    post_body['cancel_url'] = f"{main_settings.BACKEND_URL}/api/v1/payment/cancel/"
    post_body['emi_option'] = 0
    post_body['cus_name'] = f"{user.first_name} {user.last_name}"
    post_body['cus_email'] = user.email
    post_body['cus_phone'] = user.phone_number
    post_body['cus_add1'] = user.address
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = ""
    post_body['product_name'] = "Hotel Booking Website"
    post_body['product_category'] = "General"
    post_body['product_profile'] = "general"

    response = sslcz.createSession(post_body)  # API response

    if response.get("status") == 'SUCCESS':
        return Response({"payment_url": response['GatewayPageURL']})
    return Response({"error": "Payment initiation failed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def payment_success(request):
    data = request.POST
    tran_id = data.get('tran_id') # e.g., "txn_123"
    
    # 1. Extract the actual booking ID from the transaction ID
    # If your tran_id format was f"txn_{booking_id}"
    booking_id = tran_id.replace("txn_", "")

    try:
        # 2. Find the booking and update status
        booking = Booking.objects.get(id=booking_id)
        booking.is_paid = True
        booking.status = "Confirmed" # Or your preferred status
        booking.save()
        
        # 3. Redirect back to the Frontend Dashboard
        # main_settings.FRONTEND_URL should be "http://localhost:5173"
        return redirect(f"{main_settings.FRONTEND_URL}/dashboard/bookings?status=success")
        
    except Booking.DoesNotExist:
        return redirect(f"{main_settings.FRONTEND_URL}/dashboard/bookings?status=error")

 
