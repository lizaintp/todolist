from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.todolist import views

router = DefaultRouter()
router.register('task', views.TaskAPI, basename='team_api')


urlpatterns = [
    
]

urlpatterns += router.urls