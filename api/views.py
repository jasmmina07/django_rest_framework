from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task

from .serializers import TaskSerializer

class AddTask(APIView):
    def get(self, request):
        serializer=TaskSerializer(Task.objects.all(), many=True)
        return Response(serializer.data)
    

    def post(self, request):
        
        data=request.data
        serializer=TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.create(data=data)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    