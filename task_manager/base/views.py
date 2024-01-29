from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import TaskForm
from .models import Task


def homePage(request):
    context = {}
    return render(request, "base/homePage.html", context)


@login_required(login_url="login")
def dashboardPage(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    tasks = Task.objects.filter(Q(title__icontains=q))
    context = {
        "tasks": tasks,
    }
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


@login_required(login_url="login")
def createTask(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("dashboard")
        else:
            return HttpResponse("Fill up properly")

    context = {"form": form}
    return render(request, "base/CreateTask.html", context)


@login_required(login_url="login")
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.user != task.host:
        return HttpResponse("You are not Allowed Here !!!!")

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.host = request.user
            task.save()
            return redirect("dashboard")
        else:
            return HttpResponse("Fill it properly")

    context = {"form": form}
    return render(request, "base/updateTask.html", context)


@login_required(login_url="login")
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.user != task.host:
        return HttpResponse("You are not Allowed Here !!!!")

    if request.method == "POST":
        task.delete()
        return redirect("dashboard")

    return render(request, "base/DeleteTask.html", {"obj": task})
