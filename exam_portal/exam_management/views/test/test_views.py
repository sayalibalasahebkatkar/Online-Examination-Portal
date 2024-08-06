from rest_framework import viewsets
from exam_management.models import Test
from exam_management.serializers import TestSerializer,AddStudentToTestSerializer
from django.core.mail import send_mail
from exam_portal.settings import EMAIL_HOST_USER
from rest_framework.response import Response
from rest_framework import status
import sqlite3
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from django.core.files.storage import default_storage
import os
import pandas as pd
import secrets
import string


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def generate_strong_password(self, length=12):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        return password

    def create(self, request, *args, **kwargs):
        if request.data.get('has_sql'):
            db_name = request.data.get('db_name')
            sql_file = request.FILES.get('sql_file')
            
            if not sql_file:
                return Response({'error': 'No SQL file provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            if not sql_file.name.endswith('.sql'):
                return Response({'error': 'Invalid file type. Only .sql files are allowed.'}, status=status.HTTP_400_BAD_REQUEST)
            
            file_name = default_storage.save(f'{db_name}temp_sql_file.sql', sql_file)
            file_path = default_storage.path(file_name)
            
            try:
                with open(file_path, 'r') as file:
                    sql_script = file.read()
                
                conn = sqlite3.connect(db_name)
                curr = conn.cursor()
                
                sql_script_text = ''
                statements = sql_script.split(';')
                
                for statement in statements:
                    statement = statement.strip()
                    if statement:
                        try:
                            curr.execute(f"EXPLAIN QUERY PLAN {statement}")
                            curr.execute(statement)
                            sql_script_text += statement + ';'
                        except sqlite3.Error as e:
                            return Response({'statement': statement, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
                
                conn.commit()
                
                request.data['sql_script'] = sql_script_text
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            finally:
                if conn:
                    curr.close()
                    conn.close()
                if file_path and os.path.exists(file_path):
                    os.remove(file_path)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(detail=False, methods=['post'])
    def add_student(self,request):
        student_data_list = []
        if 'student_file' in request.FILES:
            student_file = request.FILES['student_file']
            student_df = pd.read_csv(student_file)
            
            student_data_list = student_df.to_dict('records')

            # Add test field to all records
            test_id = request.data.get('test')
            for student in student_data_list:
                student['test'] = test_id
                student['password'] = self.generate_strong_password()
        else:
            # Single student JSON data
            student_data = request.data.copy()
            student_data['password'] = self.generate_strong_password()
            student_data_list = [student_data]

        created_students = []
        errors = []

        for student_data in student_data_list:
            serializer = AddStudentToTestSerializer(data=student_data)
            if serializer.is_valid():
                serializer.save()
                created_students.append(serializer.data)
            else:
                errors.append({
                    'data': student_data,
                    'errors': serializer.errors
                })

        if errors:
            return Response({
                'created_students': created_students,
                'errors': errors
            }, status=status.HTTP_207_MULTI_STATUS)
        
        return Response("Students created successfully", status=status.HTTP_201_CREATED)

        


    def send_authentication_email(self,test,name,password,student_email):
        try:
            subject = "Whirlpool Aptitude Test Credentials"
            test_start_datetime = test.start_time
            test_end_datetime = test.end_time
            test_date = test_start_datetime.date()
            test_start_time = test_start_datetime.strftime('%H:%M')
            test_end_time = test_end_datetime.strftime('%H:%M')

            message = (
                f"Dear Candidate,\n\n"
                f"You are invited to participate in the Whirlpool Aptitude Test.\n\n"
                f"Test Date: {test_date}\n"
                f"Test Time: {test_start_time} to {test_end_time}\n\n"
                f"Your login credentials are as follows:\n"
                f"Username: {name}\n"
                f"Password: {password}\n\n"
                f"Best of luck!\n"
                f"Whirlpool Team"
            )
            from_email = EMAIL_HOST_USER
            recipient_list = [student_email]
            send_mail(subject,message,from_email,recipient_list)
        except Exception as e:
            print(f"Failed to send email to {student_email}: {str(e)}")  









