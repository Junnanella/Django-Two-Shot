from django.contrib import admin
from .models import Receipts, Categories, Accounts

# Register your models here.
class ReceiptsAdmin(admin.ModelAdmin):
    pass


class CategoriesAdmin(admin.ModelAdmin):
    pass


class AccountsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Receipts, ReceiptsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Accounts, AccountsAdmin)
