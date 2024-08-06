from rest_framework import serializers
from exam_management.models import Test,Student,StudentTest
from django.utils import timezone


class TestAttemptSerializer(serializers.Serializer):
    test_id = serializers.IntegerField()
    student_id = serializers.IntegerField()

    def validate(self, data):
        test_id = data.get('test_id')
        student_id = data.get('student_id')

        try:
            test = Test.objects.get(id=test_id)
            student = Student.objects.get(id=student_id)
        except Test.DoesNotExist:
            raise serializers.ValidationError("Test does not exist.")
        except Student.DoesNotExist:
            raise serializers.ValidationError("Student does not exist.")
        
        if not test.is_active:
            raise serializers.ValidationError("The test is not active at this time.")
        
        if not test.is_open:
            student_test = StudentTest.objects.filter(student=student.id, test=test.id).exists()
            if not student_test:
                raise serializers.ValidationError("Student is not eligible for this test.")
            
        # Check if the student has any ongoing tests
        ongoing_tests = StudentTest.objects.filter(
        student=student,
        started_at__isnull=False,
        completed_at__isnull=True)
        
        if ongoing_tests.exists():
            raise serializers.ValidationError("Student has an ongoing test. Cannot start a new test.")

        return data


    def create(self, validated_data):
        test = Test.objects.get(id=validated_data['test_id'])
        student = Student.objects.get(id=validated_data['student_id'])

        student_test, created = StudentTest.objects.get_or_create(
            student=student,
            test=test,
            defaults={
                'started_at': timezone.now
            }
        )

        if not created:
            if timezone.now <= test.end_time:
                student_test.started_at = timezone.now
                student_test.save()
            else:
                raise serializers.ValidationError("This test has ended and cannot be resumed.")

        return student_test
