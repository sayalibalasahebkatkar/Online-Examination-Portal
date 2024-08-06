from django.db import IntegrityError
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

from exam_management.models import Test,Student,StudentTest
from exam_management.serializers import StudentSerializer


class TestSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = Test
        fields = ['id', 'name', 'description', 'start_time', 'end_time', 'created_by', 'is_open', 'has_sql', 'db_name', 'sql_script', 'stream', 'branches', 'is_active']

    def get_is_active(self, obj):
        return obj.is_active()
    
    def validate(self, data):
        if data.get('has_sql'):
            if not data.get('db_name'):
                raise serializers.ValidationError("db_name is required when has_sql is True")
            if not data.get('sql_script'):
                raise serializers.ValidationError("sql_script is required when has_sql is True")
        else:
            data['db_name'] = None
            data['sql_script'] = None
        return data
    

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






            
    
    

    