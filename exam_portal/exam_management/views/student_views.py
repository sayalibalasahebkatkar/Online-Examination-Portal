from rest_framework import viewsets
from exam_management.models import Student
from exam_management.serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer