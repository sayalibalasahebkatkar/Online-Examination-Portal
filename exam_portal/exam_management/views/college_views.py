from rest_framework import viewsets
from rest_framework.response import Response

from exam_management.models import College,Stream,Branch,CollegeStream
from exam_management.serializers import CollegeSerializer,StreamSerializer,BranchSerializer,CollegeStreamSerializer


class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class CollegeStreamViewSet(viewsets.ModelViewSet):
    queryset = CollegeStream.objects.all()
    serializer_class = CollegeStreamSerializer