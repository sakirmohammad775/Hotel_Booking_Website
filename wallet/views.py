from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction as db_transaction
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer
from api.permissions import IsOwnerOrReadOnly


class WalletViewSet(viewsets.ModelViewSet):

    serializer_class = WalletSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["post"])
    def add_money(self, request, pk=None):

        wallet = self.get_object()
        amount = float(request.data.get("amount"))

        with db_transaction.atomic():
            wallet.balance += amount
            wallet.save()

            Transaction.objects.create(
                wallet=wallet,
                amount=amount,
                transaction_type="credit",
                description="Money added"
            )

        return Response({"status": "Money added"})

    @action(detail=True, methods=["post"])
    def deduct_money(self, request, pk=None):

        wallet = self.get_object()
        amount = float(request.data.get("amount"))

        if wallet.balance < amount:
            return Response({"error": "Insufficient balance"}, status=400)

        with db_transaction.atomic():
            wallet.balance -= amount
            wallet.save()

            Transaction.objects.create(
                wallet=wallet,
                amount=amount,
                transaction_type="debit",
                description="Booking payment"
            )

        return Response({"status": "Money deducted"})


class WalletTransactionViewSet(ReadOnlyModelViewSet):

    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(
            wallet_id=self.kwargs.get("wallet_pk")
        )