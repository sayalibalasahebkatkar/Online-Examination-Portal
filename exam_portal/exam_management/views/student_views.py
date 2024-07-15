from rest_framework import viewsets
from exam_management.models import Student
from exam_management.serializers import StudentSerializer
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.utils import timezone
import uuid
from datetime import timedelta

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer