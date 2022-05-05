from django.db import models

# import settings to access user auth
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        USER_MODEL, related_name="categories", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Accounts(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    owner = models.ForeignKey(
        USER_MODEL, related_name="accounts", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Receipts(models.Model):
    vendor = models.CharField(max_length=200)
    total = models.DecimalField(decimal_places=3, max_digits=10)
    tax = models.DecimalField(decimal_places=3, max_digits=10)
    date = models.DateField()
    purchaser = models.ForeignKey(USER_MODEL, related_name="receipts", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Categories, related_name="receipts", on_delete=models.PROTECT
    )
    account = models.ForeignKey(
        Accounts, related_name="receipts", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.vendor
