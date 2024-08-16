from rest_framework import serializers
from exam_management.models import StudentTest,Student
from exam_management.serializers import StudentSerializer

class StudentTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentTest
        fields = '__all__'
