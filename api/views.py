from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TaskSerializer

class AddTask(APIView):
    def post(self, request):
        
        data=request.data
        serializer=TaskSerializer(data=data)

        print(serializer.is_valid())
        print(serializer.create(data=data))
        return Response({"data":data})