from django.shortcuts import redirect, render
from django.urls import reverse_lazy

# import models
from receipts.models import Receipts, Categories, Accounts

# import generic views from django
from django.views.generic import ListView, CreateView

# Create your views here.

# List Views for Receipts, Categories, and Accounts
class ReceiptsListView(ListView):
    model = Receipts
    template_name = "receipts_list.html"
    context_object_name = "receipts"


class CategoriesListView(ListView):
    model = Categories
    template_name = "categories_list.html"
    context_object_name = "categories"


class AccountsListView(ListView):
    model = Accounts
    template_name = "accounts_list.html"
    context_object_name = "accounts"


# Create Views for Receipts, Categories, and Accounts
class ReceiptCreateView(CreateView):
    model = Receipts
    template_name = "receipts/receipt_create.html"
    fields = ["vendor", "total", "tax", "date", "category", "account"]

    def form_valid(self, form):
        receipt = form.save(commit=False)
        receipt.save()
        return redirect("receipts_list")
