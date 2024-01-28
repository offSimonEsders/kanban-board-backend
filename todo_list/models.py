from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=250, default=None)
    state = models.CharField(max_length=20, default='todo')
    created_at = models.DateField(default=date.today())
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    index = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.set_index()
        super(Todo, self).save(*args, **kwargs)

    def set_index(self):
        if not self.pk:
            todoMaxIndex = Todo.objects.filter(state='todo').order_by('-index').first()
            if todoMaxIndex:
                self.index = todoMaxIndex.index + 1
            else:
                self.index = 0
        else:
            pass