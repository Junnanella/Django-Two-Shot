from django.shortcuts import render

# Create your views here.
def logout(request):
    return render(request, "registration/logged_out.html")
