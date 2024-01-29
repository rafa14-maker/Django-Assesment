from django.urls import path

from . import views

urlpatterns = [
    path("tasks/", views.get_Tasks, name="tasks"),
    path("tasks/<str:pk>/", views.get_Task, name="task"),
    path("createTask/", views.createTask, name="create-task"),
    path("updateTask/<str:pk>/", views.updateTask, name="update-task"),
    path("deleteTask/<str:pk>/", views.deleteTask, name="delete-task"),
    path("registerUser/", views.registerUser, name="register-user"),
    path("me/", views.current_user, name="current-user"),
]
