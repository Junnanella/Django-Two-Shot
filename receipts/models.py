from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Accounts(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField

    def __str__(self):
        return self.name


class Receipts(models.Model):
    vendor = models.CharField(max_length=100)
    total = models.FloatField(null=False)
    tax = models.FloatField(null=False)
    date = models.DateField(null=False)
    category = models.ForeignKey(
        Category, related_name="receipts", on_delete=models.PROTECT
    )
    account = models.ForeignKey(
        Accounts, related_name="receipts", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.vendor
