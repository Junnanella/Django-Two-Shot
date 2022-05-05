# import path from django.urls
from django.urls import path

# import views
from .views import (
    ReceiptsListView,
    CategoriesListView,
    AccountsListView,
    ReceiptCreateView,
    CategoriesCreateView,
    AccountCreateView,
)

urlpatterns = [
    path("", ReceiptsListView.as_view(), name="receipts_list"),
    path("categories/", CategoriesListView.as_view(), name="categories_list"),
    path("accounts/", AccountsListView.as_view(), name="accounts_list"),
    path("create/", ReceiptCreateView.as_view(), name="receipt_create"),
    path(
        "categories/create",
        CategoriesCreateView.as_view(),
        name="category_create",
    ),
    path(
        "accounts/create", AccountCreateView.as_view(), name="account_create"
    ),
]
