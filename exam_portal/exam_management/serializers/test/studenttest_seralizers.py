from rest_framework import serializers
from exam_management.models import StudentTest,Student
from exam_management.serializers import StudentSerializer

class StudentTestSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(write_only=True, required=False)
    email = serializers.EmailField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)
    rollno = serializers.CharField(write_only=True, required=False)
    gender = serializers.CharField(write_only=True, required=False)
    highestdegree = serializers.CharField(write_only=True, required=False)
    phone_no = serializers.CharField(write_only=True, required=False)
    student = serializers.PrimaryKeyRelatedField(required=False, queryset=Student.objects.all())

    class Meta:
        model = StudentTest
        fields = '__all__'

    def create(self, validated_data):
        student_email = validated_data.get('email')
        student_fields = ['name', 'email', 'password', 'rollno', 'gender', 'highestdegree', 'phone_no']
        student_data = {field: validated_data.pop(field) for field in student_fields if field in validated_data}
        if student_email:
            try:
                student = Student.objects.get(email=student_email)
            except Student.DoesNotExist:
                student_serializer = StudentSerializer(data=student_data)
                if student_serializer.is_valid():
                    student = student_serializer.save()
                else:
                    raise serializers.ValidationError(student_serializer.errors)
            
            validated_data['student'] = student
        return super().create(validated_data)