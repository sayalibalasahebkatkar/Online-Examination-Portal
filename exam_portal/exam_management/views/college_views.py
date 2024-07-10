from rest_framework import viewsets
from exam_management.models import College,Stream,Branch
from exam_management.serializers import CollegeSerializer,StreamSerializer,BranchSerializer

class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer