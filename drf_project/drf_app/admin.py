from django.contrib import admin
from .models import Account,Wallet
# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','created_at','edited_at']

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['amount','currency','account']