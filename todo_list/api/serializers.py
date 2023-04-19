from rest_framework import serializers
from base.models import Task

class TaskSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'complete', 'created']
