from rest_framework import serializers
from django.db import transaction

from exam_management.models import Question,Option,FillInTheBlankAnswer,SqlQuery,Tag
from .option import OptionValidationSerializer
from .fib import FillInTheBlankAnswerValidationSerializer
from .sql_query import SqlQueryValidationSerializer


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionValidationSerializer(many=True,required=False)
    fill_in_blank_answer =FillInTheBlankAnswerValidationSerializer(required=False)
    sql_query = SqlQueryValidationSerializer(required=False)
    tags = serializers.ListField(
        child=serializers.CharField(max_length=50), required=False, write_only=True
    )

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_type','tags', 'options', 'fill_in_blank_answer', 'sql_query']

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
        tags_data = validated_data.pop('tags', [])

        try:
            with transaction.atomic():
                tags = []
                for tag_name in tags_data:
                    print("tag_name",tag_name)
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    tags.append(tag)
                print("tags",tags)
                
                question = Question.objects.create(**validated_data)

                # Assign tags to the question
                question.tags.set(tags)

                if question_type == 'MCQ':
                    for option_data in options_data:
                        Option.objects.create(question=question, **option_data)
                elif question_type == 'FIB':
                    FillInTheBlankAnswer.objects.create(question=question, **fill_in_blank_data)
                elif question_type == 'SQL':
                    SqlQuery.objects.create(question=question, **sql_query_data)

        except Exception as e:
            print(e)
            raise serializers.ValidationError(f"An error occurred while creating the question or tags: {str(e)}")

        return question
            
            