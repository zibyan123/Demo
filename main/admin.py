from django.contrib import admin
from .models import Wallet
from .models import History

class WalletAdmin(admin.ModelAdmin):
    list_display = ["User", "WalletAmount"]
class HistoryAdmin(admin.ModelAdmin):
    list_display = ["TransactionType", "Amount"]

admin.site.register(Wallet, WalletAdmin)
admin.site.register(History, HistoryAdmin)
