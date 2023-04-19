from rest_framework import generics, permissions
from .serializers import TaskSerializer
from base.models import Task

class TaskList(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user = user).order_by('-created')



