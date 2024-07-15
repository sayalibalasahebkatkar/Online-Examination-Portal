from rest_framework import viewsets
from rest_framework.decorators import action
from django.utils import timezone
from rest_framework import status
from exam_management.models import Test,Question,Option,FillInTheBlankAnswer,StudentTest,StudentAnswer,College,Stream,Branch,Student
from exam_management.serializers import TestSerializer, QuestionSerializer, OptionSerializer, FillInTheBlankAnswerSerializer, StudentTestSerializer, StudentAnswerSerializer,StudentSerializer
import pandas as pd
from rest_framework.response import Response
import secrets
import string
from django.core.mail import send_mail
from exam_portal.settings import EMAIL_HOST_USER
from datetime import datetime





class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    # def send_authentication_email(self,test,name,password,student_email):
    #     try:
    #         subject = "Whirlpool Aptitude Test Credentials"
    #         test_start_datetime = test.start_time
    #         test_end_datetime = test.end_time
    #         test_date = test_start_datetime.date()
    #         test_start_time = test_start_datetime.strftime('%H:%M')
    #         test_end_time = test_end_datetime.strftime('%H:%M')

    #         message = (
    #             f"Dear Candidate,\n\n"
    #             f"You are invited to participate in the Whirlpool Aptitude Test.\n\n"
    #             f"Test Date: {test_date}\n"
    #             f"Test Time: {test_start_time} to {test_end_time}\n\n"
    #             f"Your login credentials are as follows:\n"
    #             f"Username: {name}\n"
    #             f"Password: {password}\n\n"
    #             f"Best of luck!\n"
    #             f"Whirlpool Team"
    #         )
    #         from_email = EMAIL_HOST_USER
    #         recipient_list = [student_email]
    #         send_mail(subject,message,from_email,recipient_list)
    #     except Exception as e:
    #         print(f"Failed to send email to {student_email}: {str(e)}")


    # @action(detail=False,methods=['POST'])
    # def send_credentials_to_email(self,request,pk=None):
    #     try:
    #         test_id = pk
    #         print(pk)
    #         test = Test.objects.get(id=test_id)
    #         student_tests = StudentTest.objects.filter(test=test_id)
    #         # print(student_tests)
    #         for student_test in student_tests:
    #             student = student_test.student
    #             name = student.name
    #             print(name)
    #             password = student.password
    #             student_email = student.email
    #             self.send_authentication_email(test, name, password, student_email)
    #         return Response({'status': 'Emails sent successfully'}, status=status.HTTP_200_OK)

    #     except Test.DoesNotExist:
    #         return Response({'error': 'Test not found'}, status=status.HTTP_404_NOT_FOUND)
    #     except StudentTest.DoesNotExist:
    #         return Response({'error': 'No students found for this test'}, status=status.HTTP_404_NOT_FOUND)
    #     except Exception as e:
    #         print(f"An error occurred: {str(e)}")
    #         return Response({'error': 'An error occurred while sending emails'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    # @action(detail=False,methods=['POST'])
    # def addstudent(self,request,test_id=None,*args,**kwargs):

            

    
    # @action(detail=False,methods=['POST'])
    # def addstudent(self,request,test_id=None,*args,**kwargs):
    #     try:
    #         try:
    #             test = Test.objects.get(id=test_id)
    #         except Test.DoesNotExist:
    #             return Response({'error': 'Test id not found'}, status=status.HTTP_404_NOT_FOUND)
            
    #         # Check if student with given email already exists or not
    #         student_email = request.data.get('email')
    #         if Student.objects.filter(email=student_email).exists():
    #             return Response({'error': 'Student with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)


    #         student_data = {
    #         'name': request.data.get('name'),
    #         'password': self.generate_strong_password(),
    #         'rollno': request.data.get('rollno'),
    #         'email': request.data.get('email'),
    #         'gender': request.data.get('gender'),
    #         'highestdegree': request.data.get('highestdegree'),
    #         'phone_no': request.data.get('phone_no'),
    #         }

    #         student_serializer = StudentSerializer(data=student_data)
    #         if student_serializer.is_valid():
    #             print(student_serializer.validated_data)
    #             student = student_serializer.save()
    #             student_id = student.id
    #             # Create StudentTest entry
    #             student_test_data = {
    #                 'student':student_id,
    #                 'test' : test_id,
    #                 'eligible':True
    #             }
    #             student_test_serializer = StudentTestSerializer(data=student_test_data)
    #             if student_test_serializer.is_valid():
    #                 student_test = student_test_serializer.save()  # Save StudentTest instance
    #             else:
    #                 return Response(student_test_serializer.errors, status=status.HTTP_400)
    #         else:
    #             return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #         response_data = {
    #                     'message': 'Student created successfully',
    #                     'student': student_serializer.data
    #                     }
    #         return Response(response_data, status=status.HTTP_201_CREATED)
    #     except Exception as e:
    #         return Response({'error': 'Internal server error. Please try again later.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    # @action(detail=False, methods=['POST'])
    # def addStudentscsv(self, request,pk=None):
    #     try:
    #         test_id = pk
    #     except Test.DoesNotExist:
    #         return Response({'error': 'Test id not found'}, status=status.HTTP_404_NOT_FOUND)
        
    #     test = Test.objects.get(id=test_id)
    #     has_eligibility_criteria=test.has_eligibility_criteria
    #     if not has_eligibility_criteria:
    #         return Response({'error': 'Test is open for all students'}, status=status.HTTP_400_BAD_REQUEST)
        
    #     file = request.data.get('file')
    #     df = pd.read_csv(file)
            
    #     for index, row in df.iterrows():
    #         print(row)
    #         student_data = {
    #             'name': row['name'],
    #             'password': self.generate_strong_password(),
    #             'rollno': row['rollno'],
    #             'email': row['email'],
    #             'gender': row['gender'],
    #             'highestdegree': row['highestdegree'],
    #             'phone_no': row['phone_no'],
    #         }
    #         student_serializer = StudentSerializer(data=student_data)
    #         if student_serializer.is_valid():
    #             student = student_serializer.save()  # Save Student instance
    #             student_id = student.id  

    #             # Create StudentTest entry
    #             student_test_data = {
    #                 'student': student_id,  
    #                 'test': test_id,
    #                 'eligible': True,  
    #             }
    #             student_test_serializer = StudentTestSerializer(data=student_test_data)
    #             if student_test_serializer.is_valid():
    #                 student_test = student_test_serializer.save()  # Save StudentTest instance
    #             else:
    #                 return Response(student_test_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #         else:
    #             return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     response_data = {
    #     'message': 'Students created successfully'
    #     }
        # return Response(response_data, status=status.HTTP_201_CREATED)

            
        
    
        
        

        

    # def create(self, request, *args, **kwargs):
    #     file = request.data.pop('file', None)
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
        
    #     test = serializer.save()
    #     if serializer.validated_data.get('has_eligibility_criteria'):
    #         df = pd.read_csv(file[0])
            
    #         for index, row in df.iterrows():
    #             print(row)
    #             student_data = {
    #                 'name': row['name'],
    #                 'password': self.generate_strong_password(),
    #                 'rollno': row['rollno'],
    #                 'email': row['email'],
    #                 'gender': row['gender'],
    #                 'highestdegree': row['highestdegree'],
    #                 'phone_no': row['phone_no'],
    #             }
    #             print(student_data)


    #             # Send Credentials to given Email
    #             test_start_datetime = serializer.validated_data.get('start_time')
    #             test_end_datetime = serializer.validated_data.get('end_time')
    #             test_date = test_start_datetime.date()
    #             test_start_time = test_start_datetime.strftime('%H:%M')
    #             test_end_time=test_end_datetime.strftime('%H:%M')

    #             self.send_credentials_to_email(test_date,test_start_time,test_end_time,student_data['name'],student_data['password'],student_data['email'])


    #             student_serializer = StudentSerializer(data=student_data)
    #             if student_serializer.is_valid():
    #                 student_serializer.save()
    #             else:
    #                 return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    




class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class FillInTheBlankAnswerViewSet(viewsets.ModelViewSet):
    queryset = FillInTheBlankAnswer.objects.all()
    serializer_class = FillInTheBlankAnswerSerializer


class StudentTestViewSet(viewsets.ModelViewSet):
    queryset = StudentTest.objects.all()
    serializer_class = StudentTestSerializer

    def generate_strong_password(self, length=12):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        return password

    @action(detail=False,methods=['POST'])
    def addstudentToTest(self,request,*args,**kwargs):
        data=request.data
        data['password']=self.generate_strong_password()
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class StudentAnswerViewSet(viewsets.ModelViewSet):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer