from rest_framework import viewsets
from exam_management.models import Question
from exam_management.serializers import  QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer