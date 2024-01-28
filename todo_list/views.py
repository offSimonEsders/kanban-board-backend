from django.shortcuts import render

from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .serializers import TodoSerializer
from .models import Todo
import json


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('index')
    serializer_class = TodoSerializer
    permission_classes = []

    def get(self, request, format=None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        todossend = json.loads(request.body)
        for todo in todossend:
            updateTodo(todo)
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response({'updated': serializer.data, 'data': todossend})


def updateTodo(todosend: dict):
    todo = Todo.objects.get(id=todosend['id'])
    todo.title = todosend['title']
    todo.description = todosend['description']
    todo.state = todosend['state']
    todo.index = todosend['index']
    todo.save()
    return todo
