from django.shortcuts import render
from rest_framework import status, permissions, viewsets, mixins, response
from core.models import Todo
from core.serilaizers import TodoSerilaizer
from django.http import HttpResponse

# Authentication view
def auth_view(request):
    return HttpResponse("This is the authentication view.")

# ViewSet for Todo model
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerilaizer  
