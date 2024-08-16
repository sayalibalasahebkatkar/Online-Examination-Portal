from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from exam_management.models import Test, Question,TestQuestion
from exam_management.serializers import QuestionSerializer,TestQuestionSerializer

class TestQuestionViewset(ViewSet):

    def add_question_to_test(self,request,test_id):
        try:
            test = Test.objects.get(id = test_id)
            if not test:
                return Response({"error": "Test not found."}, status=status.HTTP_404_NOT_FOUND)

            # If a question_id is provided, associate it with the test
            question_id = request.data.get('question_id')
            if not question_id:
                # Extract question details from the request
                question_text = request.data.get('question_text')
                question_type = request.data.get('question_type')

                if not question_text or not question_type:
                    return Response({"error": "Question text and type are required."}, status=status.HTTP_400_BAD_REQUEST)
                
                # Check if the question already exists
                question = Question.objects.filter(question_text=question_text, question_type=question_type).first()
                if not question:
                    question_serializer = QuestionSerializer(data=request.data)
                    question_serializer.is_valid(raise_exception=True)
                    question = question_serializer.save()
                
                question_id = question.id

            test_question_data = {
                "test" :test_id,
                "question" : question_id}
            
            test_question_serializer = TestQuestionSerializer(data=test_question_data)
            test_question_serializer.is_valid(raise_exception=True)
            test_question_serializer.save()
            return Response({"message": "Question created and added to test successfully."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def get_test_question(self, request, test_id=None):
        try:
            test = Test.objects.get(id=test_id)
            if not test:
                return Response({'error': 'Test not found'}, status=404)

            test_questions = TestQuestion.objects.filter(test=test)
            if not test_questions.exists():
                return Response({"message": "No questions found for this test."}, status=status.HTTP_200_OK)
            
            # Serialize the questions
            question_serializer = QuestionSerializer([tq.question for tq in test_questions], many=True)
            return Response(question_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                    






