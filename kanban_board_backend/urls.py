"""
URL configuration for kanban_board_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from todo_list.views import TodoViewSet, LoginViewSet, CheckTokenViewSet, RegisterViewSet, LogoutViewSet, \
    CreateTodoViewSet, DeleteTodoViewSet

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('login/', LoginViewSet.as_view(), name='login'),
    path('checkToken/', CheckTokenViewSet.as_view(), name='checkToken'),
    path('register/', RegisterViewSet.as_view(), name='register'),
    path('logout/', LogoutViewSet.as_view(), name='logout'),
    path('createTodo/', CreateTodoViewSet.as_view(), name='createTodo'),
    path('delete/', DeleteTodoViewSet.as_view(), name='delete'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
