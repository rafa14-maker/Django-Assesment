from django.urls import path

from . import views

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("login/", views.loginUser, name="login"),
    path("register/", views.RegisterUser, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path("dashboard/", views.dashboardPage, name="dashboard"),
]
