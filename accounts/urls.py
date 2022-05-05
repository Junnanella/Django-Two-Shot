# import path from django.urls
from django.urls import path

# import views - login and logout are builtin views with Django
from django.contrib.auth.views import LoginView, LogoutView

# import a view for signup

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # add path for signup
]
