from django.contrib import admin
from .models import Wallet, Transaction


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("user", "balance", "updated_at")
    search_fields = ("user__email",)
    readonly_fields = ("updated_at",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("wallet", "transaction_type", "amount", "created_at")
    list_filter = ("transaction_type",)
    search_fields = ("wallet__user__email",)
    readonly_fields = ("created_at",)