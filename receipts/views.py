from django.shortcuts import redirect, render
from django.urls import reverse_lazy

# import models
from receipts.models import Receipts, Categories, Accounts

# import generic views from django
from django.views.generic import ListView, CreateView

# import Login requirements
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# List Views for Receipts, Categories, and Accounts
class ReceiptsListView(ListView):
    model = Receipts
    template_name = "receipts/receipts_list.html"
    context_object_name = "receipts"

    def get_queryset(self):
        return Receipts.objects.filter(purchaser=self.request.user)


class CategoriesListView(ListView):
    model = Categories
    template_name = "receipts/categories_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Categories.objects.filter(owner=self.request.user)


class AccountsListView(ListView):
    model = Accounts
    template_name = "receipts/accounts_list.html"
    context_object_name = "accounts"

    def get_queryset(self):
        return Accounts.objects.filter(owner=self.request.user)


# Create Views for Receipts, Categories, and Accounts
class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipts
    template_name = "receipts/receipt_create.html"
    fields = ["vendor", "total", "tax", "date", "category", "account"]

    def form_valid(self, form):
        receipt = form.save(commit=False)
        receipt.purchaser = self.request.user
        receipt.save()
        return redirect("receipts_list")


class CategoriesCreateView(LoginRequiredMixin, CreateView):
    model = Categories
    template_name = "receipts/category_create.html"
    fields = ["name"]

    def form_valid(self, form):
        category = form.save(commit=False)
        category.owner = self.request.user
        category.save()
        return redirect("categories_list")


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Accounts
    template_name = "receipts/account_create.html"
    fields = ["name", "number"]

    def form_valid(self, form):
        account = form.save(commit=False)
        account.owner = self.request.user
        account.save()
        return redirect("accounts_list")
