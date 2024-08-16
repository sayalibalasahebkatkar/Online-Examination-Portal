from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.utils import timezone

from exam_management.models import StudentTest,Test

class IsStudentEligibleForTest(BasePermission):
    def has_permission(self, request, view):
        # Extract the student ID from the JWT token
        # student_id = request.user.id

        student_id=None
        if 'student_id' in request.query_params:
            student_id = request.query_params['student_id']
        
        if not student_id:
            raise PermissionDenied("student ID not provided")

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
        
        # Retrieve the test object
        try:
            test = Test.objects.get(id=test_id)
        except Test.DoesNotExist:
            raise PermissionDenied("Test does not exist")
                
        # If the test is open, create a StudentTest entry if it doesn't exist
        if test.is_open:
            student_test, created = StudentTest.objects.get_or_create(
                student_id=student_id,
                test_id=test_id,
                defaults={'started_at': timezone.now()}
            )
            return True
    
        # Check if the student is eligible for the test
        try:
            student_test = StudentTest.objects.get(student_id=student_id, test_id=test_id)
        except StudentTest.DoesNotExist:
            raise PermissionDenied("Student is not eligible for this test")

        return True
