from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from exam_management.serializers import TestAttemptSerializer

class StartTestView(APIView):
    def post(self, request):
        serializer = TestAttemptSerializer(data=request.data)
        if serializer.is_valid():
            try:
                student_test = serializer.save()
                return Response({
                    "message": "Test started or resumed successfully",
                    "start_time": student_test.started_at
                }, status=status.HTTP_201_CREATED)
            except serializers.ValidationError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)