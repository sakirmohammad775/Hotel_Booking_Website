from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Room
from .serializers import RoomSerializer
from api.permissions import IsAdminOrReadOnly


class RoomViewSet(ModelViewSet):

    queryset = Room.objects.select_related("hotel").all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]