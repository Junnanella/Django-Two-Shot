from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logout(request):
    return render(request, "registration/logged_out.html")


def signup(request):
    # if the request method is "POST", then
    if request.method == "POST":
        #     form = UserCreationForm(request.POST)
        form = UserCreationForm(request.POST)
        #     if the form is valid, then
        if form.is_valid():
            #         username = the "username" value from the request.POST dictionary
            username = request.POST.get("username")
            #         password = the "password1" value from the request.POST dictionary
            password = request.POST.get("password")
            #         user = create a new user using username and password
            user = User.objects.create_user(
                username=username,
                password=password,
            )
            #         save the user object
            user.save()
            #         login the user with the request and user object
            login(request, user)
            #         return a redirect to the "home" path
            return redirect("/")
        # otherwise,
    else:
        #     form = UserCreationForm(request.POST)
        form = UserCreationForm()
        # context = dictionary with key "form" and value form
    context = {
        "form": form,
    }
    # return render with request, "registration/signup.html", and the context
    return render(request, "registration/signup.html", context)
