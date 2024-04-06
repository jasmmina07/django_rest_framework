from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task



class TaskSerializer(serializers.Serializer):
    title = serializers.CharField()
    completed = serializers.BooleanField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()

    def create(self, data):
        print(data)
        return {}