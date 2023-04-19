from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.TaskListCreate.as_view()),
    path('tasks/completed', views.TaskCompletedList.as_view()),
]