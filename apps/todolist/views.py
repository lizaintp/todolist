from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
# Create your views here.

from apps.todolist import models
from apps.todolist import serializer

class TaskAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = models.Task.objects.all()
    serializer_class = serializer.TaskSerializer