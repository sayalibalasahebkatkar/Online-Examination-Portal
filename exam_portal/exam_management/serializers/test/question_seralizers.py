from rest_framework import serializers
from exam_management.models import Question,Option,FillInTheBlankAnswer,SqlQuery
from .option_seralizers import OptionValidationSerializer
from .fillintheblanks_serializers import FillInTheBlankAnswerValidationSerializer
from .sqlquery_serializers import SqlQueryValidationSerializer


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionValidationSerializer(many=True,required=False)
    fill_in_blank_answer =FillInTheBlankAnswerValidationSerializer(required=False)
    sql_query = SqlQueryValidationSerializer(required=False)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_type', 'test', 'options', 'fill_in_blank_answer', 'sql_query']

    def validate(self, data):
        question_type = data['question_type']

        if question_type=='MCQ':
            options_data = data.get('options',None)
            if not options_data:
                raise serializers.ValidationError("Options are required for MCQ questions.")
        elif question_type == 'FIB':
            fill_in_blank_data = data.get('fill_in_blank_answer',None)
            if not fill_in_blank_data:
                raise serializers.ValidationError("Fill in the blank answer is required for FIB questions.")
        elif question_type=='SQL':
            sql_query_data = data.get('sql_query',None)
            if not sql_query_data:
                raise serializers.ValidationError("SQL query is required for SQL questions.")
            
        return super().validate(data)

        
        
    def create(self, validated_data):
        question_type = validated_data['question_type']
        
        options_data = validated_data.pop('options', None)
        fill_in_blank_data = validated_data.pop('fill_in_blank_answer', None)
        sql_query_data = validated_data.pop('sql_query', None)

        question = Question.objects.create(**validated_data)

        if question_type == 'MCQ':
            for option_data in options_data:
                Option.objects.create(question=question, **option_data)
        elif question_type == 'FIB':
            FillInTheBlankAnswer.objects.create(question=question, **fill_in_blank_data)
        elif question_type == 'SQL':
            SqlQuery.objects.create(question=question, **sql_query_data)

        return question