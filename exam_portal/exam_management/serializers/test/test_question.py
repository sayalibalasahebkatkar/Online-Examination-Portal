from rest_framework import serializers

from exam_management.models import TestQuestion

class TestQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = '__all__'