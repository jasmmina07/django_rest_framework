from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task



class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    completed = serializers.BooleanField(default=False)
    description = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Task
        fields = "__all__"

    def create(self, data):
        print(data)
        Task.objects.create(**data)
        return "Done"