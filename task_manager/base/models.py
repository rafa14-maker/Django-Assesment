from django.contrib.auth.models import User
from django.db import models

# Create your models here.

priority_choices = [
    (1, "low"),
    (2, "Medium"),
    (3, "Hight"),
]


class Task(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    task_complete = models.BooleanField(default=False)
    task_due_date = models.DateField(blank=True, null=True)
    priority = models.IntegerField(choices=priority_choices, default=1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-priority", "-updated", "-created", "-task_complete"]

    def __str__(self):
        return self.title
