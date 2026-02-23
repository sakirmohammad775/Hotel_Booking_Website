from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "room", "check_in_date", "check_out_date", "total_price", "status", "created_at")
    list_filter = ("status", "check_in_date", "check_out_date")
    search_fields = ("user__email", "room__room_number", "room__hotel__name")
    readonly_fields = ("created_at",)