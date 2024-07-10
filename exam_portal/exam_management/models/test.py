from django.db import models
from admin import Admin
from student import Student
from datetime import datetime
from ..enums import QuestionType
from college import Branch,Stream


class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(Admin, on_delete=models.CASCADE)

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_type = models.CharField(max_length=30, choices=[(tag.value, tag.name) for tag in QuestionType])
    question_text = models.TextField()
    question_type = models.CharField(max_length=30, choices=question_type)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

class Option(models.Model):
    id = models.AutoField(primary_key=True)
    option_text = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class FillInTheBlankAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct_answer = models.TextField()

class StudentTest(models.Model):
    id = models.AutoField(primary_key=True)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

class StudentAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_answer = models.TextField(null=True, blank=True)
    answered_at = models.DateTimeField(auto_now_add=True)
    student_test = models.ForeignKey(StudentTest, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, null=True, blank=True, on_delete=models.SET_NULL)