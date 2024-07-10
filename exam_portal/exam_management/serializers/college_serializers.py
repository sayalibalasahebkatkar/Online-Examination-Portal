from rest_framework import serializers
from exam_management.models import College,Stream,Branch

class CollegeSerializer(serializers.ModelSerializer):
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), many=True)

    class Meta:
        model = College
        fields = '__all__'


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

