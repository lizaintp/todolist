from django.contrib import admin
from apps.todolist import models

# Register your models here.

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'completed')
    