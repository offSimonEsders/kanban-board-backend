from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate, login

from .serializers import TodoSerializer, UserSerializer
from .models import Todo
import json


class LoginViewSet(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        token, create = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data})

class RegisterViewSet(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        User.objects.create_user(username=username, password=password)
        return Response('')

class LogoutViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        token = json.loads(request.body)
        Token.objects.filter(key=token).delete()
        return Response('')

class CheckTokenViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        return Response('')

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('index')
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    """
        def get(self, request, format=None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    """

    def put(self, request, format=None):
        todossend = json.loads(request.body)
        for todo in todossend:
            updateTodo(todo)
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response({'updated': serializer.data, 'data': todossend})

class CreateTodoViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        data = json.loads(request.body)
        title = data['title']
        description = data['description']
        user = request.user
        todo = Todo.objects.create(title=title, description=description, creator=user)
        serializer = TodoSerializer(todo, many=False)
        return Response({'created': serializer.data})

class EditSingleTodoViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        data = json.loads(request.body)
        todo = Todo.objects.get(id=data['id'])
        todo.title = data['title']
        todo.description = data['description']
        todo.save()
        return Response('')

class DeleteTodoViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        id = json.loads(request.body)
        Todo.objects.filter(id=id).delete()
        return Response('')

def updateTodo(todosend: dict):
    todo = Todo.objects.get(id=todosend['id'])
    todo.title = todosend['title']
    todo.description = todosend['description']
    todo.state = todosend['state']
    todo.index = todosend['index']
    todo.save()
    return todo
