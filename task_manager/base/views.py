from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def homePage(request):
    context = {}
    return render(request, "base/homePage.html", context)


def dashboardPage(request):
    context = {}
    return render(request, "base/dashboard.html", context)


def logoutUser(request):
    logout(request)
    return redirect("homePage")


def loginUser(request):
    page = "login"
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exists")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "User or password does not match")

    context = {"page": page}
    return render(request, "base/login_registration.html", context)


def RegisterUser(request):
    page = "register"
    form = UserCreationForm

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Fill out the cloumns properly")
    context = {"page": page, "form": form}
    return render(request, "base/login_registration.html", context)
