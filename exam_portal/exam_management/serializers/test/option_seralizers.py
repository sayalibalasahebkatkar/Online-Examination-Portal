from rest_framework import serializers
from exam_management.models import Option,Question

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class OptionValidationSerializer(OptionSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), required=False)