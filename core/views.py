from django.shortcuts import render

from rest_framework import (
    status,
    permissions,
    viewsets,
    mixins,
    response,
    request
)

from core.models import Todo
from core.serilaizers import TodoSerilaizer


# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerilaizer