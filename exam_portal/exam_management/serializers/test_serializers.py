from rest_framework import serializers
from exam_management.models import Test,Question,Option,FillInTheBlankAnswer,StudentTest,StudentAnswer

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'


class FillInTheBlankAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FillInTheBlankAnswer
        fields = '__all__'


class StudentTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTest
        fields = '__all__'


class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = '__all__'