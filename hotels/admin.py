from django.contrib import admin
from .models import Hotel, Review


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "price_per_night", "available_rooms", "created_at")
    search_fields = ("name", "location")
    readonly_fields = ("created_at",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("hotel", "user", "rating", "created_at")
    search_fields = ("hotel__name", "user__email")
    readonly_fields = ("created_at",)