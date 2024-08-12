from rest_framework import serializers
from exam_management.models import College,Stream,Branch,CollegeStream
from rest_framework.exceptions import APIException


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class CollegeSerializer(serializers.ModelSerializer):
    college_streams = serializers.SerializerMethodField()
    class Meta:
        model = College
        fields = ['id', 'name', 'address', 'registered_by', 'college_streams']

    def get_college_streams(self, obj):
        try:
            college_streams = CollegeStream.objects.filter(college=obj).prefetch_related('stream', 'branches')
            print(college_streams)
            streams = []

            for cs in college_streams:
                stream_name = cs.stream.name
                branch_names = list(cs.branches.values_list('name', flat=True))

                streams.append({
                    "stream_name": stream_name,
                    "stream_branches": branch_names
                })

            return streams

        except Exception as e:
            raise APIException(f"Error fetching college streams: {str(e)}")

    
    

class CollegeStreamSerializer(serializers.ModelSerializer):
    stream = serializers.PrimaryKeyRelatedField(queryset=Stream.objects.all())
    branches = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), many=True)

    class Meta:
        model = CollegeStream
        fields = ['id', 'college', 'stream', 'branches']





