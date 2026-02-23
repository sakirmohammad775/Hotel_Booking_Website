from django.contrib import admin
from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("hotel", "room_number", "room_type", "price_per_night", "capacity", "is_available", "created_at")
    list_filter = ("room_type", "is_available")
    search_fields = ("hotel__name", "room_number")
    readonly_fields = ("created_at",)