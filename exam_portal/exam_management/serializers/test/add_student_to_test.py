from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from rest_framework import serializers



from exam_management.serializers import StudentSerializer
from exam_management.models import Student,Test,StudentTest


class AddStudentToTestSerializer(serializers.Serializer):
    name = serializers.CharField(write_only=True, required=False)
    email = serializers.EmailField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)
    rollno = serializers.CharField(write_only=True, required=False)
    gender = serializers.CharField(write_only=True, required=False)
    highestdegree = serializers.CharField(write_only=True, required=False)
    phone_no = serializers.CharField(write_only=True, required=False)
    student = serializers.PrimaryKeyRelatedField(required=False, queryset=Student.objects.all())
    test = serializers.PrimaryKeyRelatedField(required=False, queryset=Test.objects.all())


    def validate(self, data):
        if 'student' not in data and 'email' not in data:
            raise  serializers.ValidationError("Either existing student ID or new student details must be provided.")
        return data

    def create(self, validated_data):
        test = validated_data['test']

        if test.is_open:
            raise serializers.ValidationError("This function is only for closed tests.")
        
        try:
            if 'student' in validated_data:
                student = validated_data['student']
            else:
                student_data = {k: v for k, v in validated_data.items() if k != 'test'}
                student_serializer = StudentSerializer(data=student_data)
                try:
                    student_serializer.is_valid(raise_exception=True)
                    student = student_serializer.save()
                except serializers.ValidationError as e:
                    raise serializers.ValidationError({"student": e.detail})
                except IntegrityError as e:
                    raise serializers.ValidationError({"student": f"IntegrityError: {str(e)}"})

            try:
                student_test = StudentTest.objects.get_or_create(
                    student=student,
                    test=test
                )
            except IntegrityError as e:
                raise serializers.ValidationError({"student_test": f"IntegrityError: {str(e)}"})

            return {'student': student, 'student_test': student_test}

        except ObjectDoesNotExist as e:
            raise serializers.ValidationError({"error": f"ObjectDoesNotExist: {str(e)}"})
        except Exception as e:
            raise serializers.ValidationError({"error": f"An unexpected error occurred: {str(e)}"})






            
    
    

    