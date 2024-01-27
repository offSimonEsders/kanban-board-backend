from django.contrib import admin

from todo_list.models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    fields = ['__all__']
    list_display = ['id', 'title', 'description', 'state', 'created_at', 'creator', 'index']

admin.site.register(Todo, TodoAdmin)