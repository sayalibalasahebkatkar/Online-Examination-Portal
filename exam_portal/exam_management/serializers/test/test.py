from rest_framework import serializers
from django.utils import timezone

from exam_management.models import Test


class TestSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = Test
        fields = ['id', 'name', 'description', 'start_time', 'end_time', 'created_by', 'is_open', 'has_sql', 'db_name', 'sql_script', 'stream', 'branches', 'is_active']

    def get_is_active(self, obj):
        return obj.is_active()
    
    def validate_start_time(self, value):
        """
        Check that the start_time is not in the past.
        """
        now = timezone.now()
        if value < now:
            raise serializers.ValidationError("Start time cannot be in the past.")
        return value
    
    def validate(self, data):
        if data['start_time'] > data['end_time']:
            raise serializers.ValidationError("End time cannot be before the start time.")

        if data.get('has_sql'):
            if not data.get('db_name'):
                raise serializers.ValidationError("db_name is required when has_sql is True")
            if not data.get('sql_script'):
                raise serializers.ValidationError("sql_script is required when has_sql is True")
        else:
            data['db_name'] = None
            data['sql_script'] = None
        return data
    

