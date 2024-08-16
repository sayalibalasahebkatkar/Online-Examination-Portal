from rest_framework import viewsets
from exam_management.serializers import  StudentTestSerializer
from exam_management.models import StudentTest


class StudentTestViewSet(viewsets.ModelViewSet):
    queryset = StudentTest.objects.all()
    serializer_class = StudentTestSerializer

