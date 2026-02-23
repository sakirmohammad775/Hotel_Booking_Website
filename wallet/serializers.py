from rest_framework import serializers
from .models import Wallet, Transaction
from users.models import User


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "wallet", "amount", "transaction_type", "description", "created_at"]
        read_only_fields = ["wallet", "created_at"]


class WalletSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)  # show user email

    class Meta:
        model = Wallet
        fields = ["id", "user", "balance", "transactions"]