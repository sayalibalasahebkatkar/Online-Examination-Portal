from rest_framework import viewsets
from exam_management.models import Option
from exam_management.serializers import OptionSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer