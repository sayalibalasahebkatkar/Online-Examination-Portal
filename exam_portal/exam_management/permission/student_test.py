from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from exam_management.models import StudentTest,Test
from django.shortcuts import get_object_or_404

class IsStudentEligibleForTest(BasePermission):
    def has_permission(self, request, view):
        # Extract the student ID from the JWT token
        # student_id = request.user.id
        student_id=5

        # Retrieve the test ID from the request
        test_id = None
        if 'test_id' in request.data:
            test_id = request.data['test_id']
        elif 'test_id' in request.query_params:
            test_id = request.query_params['test_id']
        elif 'test_id' in view.kwargs:
            test_id = view.kwargs['test_id']

        if not test_id:
            raise PermissionDenied("Test ID not provided")
    
        # Check if the student is eligible for the test
        try:
            student_test = StudentTest.objects.get(student_id=student_id, test_id=test_id)
        except StudentTest.DoesNotExist:
            raise PermissionDenied("Student is not eligible for this test")

        return True
