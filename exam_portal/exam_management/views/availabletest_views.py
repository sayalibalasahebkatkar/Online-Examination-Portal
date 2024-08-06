from rest_framework import viewsets, permissions
from rest_framework.response import Response
from exam_management.models import Test,Student
from exam_management.serializers import AvailableTestSerializer

class AvailableTestViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AvailableTestSerializer

    def get_queryset(self):
        return Test.objects.all()

    def list(self, request, *args, **kwargs):
        student_id = request.data.get('student_id')
        if not student_id:
            return Response({"error": "Student ID is required"}, status=400)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'student_id': student_id})

        grouped_tests = {
            "Upcoming": [],
            "Ongoing": [],
            "Completed": []
        }
        
        for test in serializer.data:
            if test['is_open'] or test['is_eligible']:
                grouped_tests[test['status']].append(test)

        response_data = {
            "tests": grouped_tests
        }

        return Response(response_data)