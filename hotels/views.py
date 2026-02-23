from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Hotel, Review
from .serializers import HotelSerializer, ReviewSerializer
from api.permissions import IsAdminOrReadOnly


class HotelViewSet(ModelViewSet):

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ["name", "location"]


class ReviewViewSet(ModelViewSet):

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Review.objects.filter(hotel_id=self.kwargs.get("hotel_pk"))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)