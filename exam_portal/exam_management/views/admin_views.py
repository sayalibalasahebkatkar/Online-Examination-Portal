from rest_framework import viewsets
from exam_management.models import Admin
from exam_management.serializers import AdminSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
