from rest_framework import viewsets
from exam_management.models import Test,Question,Option,FillInTheBlankAnswer,StudentTest,StudentAnswer
from exam_management.serializers import TestSerializer, QuestionSerializer, OptionSerializer, FillInTheBlankAnswerSerializer, StudentTestSerializer, StudentAnswerSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class FillInTheBlankAnswerViewSet(viewsets.ModelViewSet):
    queryset = FillInTheBlankAnswer.objects.all()
    serializer_class = FillInTheBlankAnswerSerializer

class StudentTestViewSet(viewsets.ModelViewSet):
    queryset = StudentTest.objects.all()
    serializer_class = StudentTestSerializer

class StudentAnswerViewSet(viewsets.ModelViewSet):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer