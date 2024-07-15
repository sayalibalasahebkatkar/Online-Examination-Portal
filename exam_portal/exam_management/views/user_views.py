from rest_framework import viewsets
from exam_management.models import User
from exam_management.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer