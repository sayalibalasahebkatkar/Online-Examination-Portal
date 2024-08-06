from rest_framework import viewsets
from exam_management.models import StudentAnswer
from exam_management.serializers import  StudentAnswerSerializer

class StudentAnswerViewSet(viewsets.ModelViewSet):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
