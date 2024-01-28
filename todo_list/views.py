from django.shortcuts import render

from rest_framework import permissions, viewsets

from .serializers import TodoSerializer
from .models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('index')
    serializer_class = TodoSerializer
    permission_classes = []
