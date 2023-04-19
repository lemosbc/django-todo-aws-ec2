from rest_framework import generics, permissions
from .serializers import TaskSerializer
from base.models import Task

class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user = user, complete = False).order_by('-created')

class TaskCompletedList(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user = user, complete = True).order_by('-created')
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



