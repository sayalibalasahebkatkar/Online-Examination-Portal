from rest_framework import serializers
from exam_management.models import SqlQuery,Question

class SqlQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = SqlQuery
        fields = '__all__'
    
class SqlQueryValidationSerializer(SqlQuerySerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), required=False)
