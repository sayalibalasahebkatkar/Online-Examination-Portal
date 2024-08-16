from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone


from rest_framework import viewsets
from exam_management.models import Question,Test,StudentTest
from exam_management.serializers import  QuestionSerializer
from exam_management.permission import IsStudentEligibleForTest


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [IsStudentEligibleForTest]

    @action(detail=False, methods=['get'], url_path='test-questions')
    def get_test_question(self, request, test_id=None):
        test_id = request.query_params.get('test_id')
        try:
            test = Test.objects.get(id=test_id)
        except Test.DoesNotExist:
            return Response({'error': 'Test not found'}, status=404)

        questions = self.queryset.filter(test=test)
        serializer = self.get_serializer(questions, many=True)
        return Response(serializer.data)
