from django.urls import path, include
from rest_framework_nested import routers

from hotels.views import HotelViewSet
from rooms.views import RoomViewSet
from bookings.views import BookingViewSet
from wallet.views import WalletViewSet, WalletTransactionViewSet
from hotels.views import ReviewViewSet

router = routers.DefaultRouter()

# Main routes
router.register("hotels", HotelViewSet, basename="hotels")
router.register("rooms", RoomViewSet, basename="rooms")
router.register("bookings", BookingViewSet, basename="bookings")
router.register("wallets", WalletViewSet, basename="wallets")

# Nested routes
hotel_router = routers.NestedSimpleRouter(router, "hotels", lookup="hotel")
hotel_router.register("reviews", ReviewViewSet, basename="hotel-reviews")

wallet_router = routers.NestedSimpleRouter(router, "wallets", lookup="wallet")
wallet_router.register("transactions", WalletTransactionViewSet, basename="wallet-transactions")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(hotel_router.urls)),
    path("", include(wallet_router.urls)),

    # Auth
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]