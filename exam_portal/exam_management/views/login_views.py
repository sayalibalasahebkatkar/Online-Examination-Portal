from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from exam_management.utils import generate_access_token
from exam_management.models import User,Student

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        is_student = request.data.get('is_student')
        try:
            if is_student:
                user = Student.objects.get(email=email)
            else:
                user = User.objects.get(email=email)
            if check_password(password, user.password):
                token = generate_access_token(user,is_student)
                return Response({'token': token}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

