from rest_framework import serializers
from django.contrib.auth.models import User
from todo_list.models import Todo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id']

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    creator = UserSerializer(read_only=True)
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'state', 'created_at', 'creator', 'index']