from rest_framework import serializers
from exam_management.models import FillInTheBlankAnswer,Question


class FillInTheBlankAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FillInTheBlankAnswer
        fields = '__all__'


class FillInTheBlankAnswerValidationSerializer(FillInTheBlankAnswerSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), required=False)
