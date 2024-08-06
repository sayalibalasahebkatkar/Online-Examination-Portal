from rest_framework import serializers
from exam_management.models import User
# from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


