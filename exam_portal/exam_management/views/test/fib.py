from rest_framework import viewsets
from exam_management.models import FillInTheBlankAnswer
from exam_management.serializers import FillInTheBlankAnswerSerializer

class FillInTheBlankAnswerViewSet(viewsets.ModelViewSet):
    queryset = FillInTheBlankAnswer.objects.all()
    serializer_class = FillInTheBlankAnswerSerializer
