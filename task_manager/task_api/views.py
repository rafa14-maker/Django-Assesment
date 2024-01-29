from base.models import Task
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
from .serializers import SignupSerializer, TaskSerializer, UserSerializer


@api_view(["GET"])
def get_Tasks(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response({"Tasks": serializer.data})


@api_view(["GET"])
def get_Task(request, pk):
    task = get_object_or_404(Task, id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response({"Tasks": serializer.data})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createTask(request):
    data = request.data
    serializer = TaskSerializer(data=data)

    if serializer.is_valid():
        task = Task.objects.create(**data, host=request.user)
        res = TaskSerializer(task, many=False)
        return Response({"Task": res.data})
    else:
        return Response(serializer.errors)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    serializer = TaskSerializer(task, many=False)

    if task.host != request.user:
        return Response(
            {"error": "You cannot update this product"},
            status=status.HTTP_403_FORBIDDEN,
        )

    task.title = request.data["title"]
    task.description = request.data["description"]
    task.task_complete = request.data["task_complete"]
    task.task_due_date = request.data["task_due_date"]
    task.priority = request.data["priority"]
    task.save()

    res = TaskSerializer(task, many=False)
    return Response({"Task": res.data})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def deleteTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    serializer = TaskSerializer(task, many=False)

    if task.host != request.user:
        return Response(
            {"error": "You cannot delete this product"},
            status=status.HTTP_403_FORBIDDEN,
        )

    task.delete()
    return Response("Task Deleted")


@api_view(["POST"])
def registerUser(request):
    data = request.data
    user = SignupSerializer(data=data)

    if user.is_valid():
        if not User.objects.filter(username=data["username"]).exists():
            user = User.objects.create(
                username=data["username"],
                password=make_password(
                    data["password"],
                ),
            )
            return Response(
                {"details": "User Registered"}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(user.error)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = UserSerializer(request.user, many=False)
    return Response(user.data)
