from django.db import models
from .student_test import StudentTest
from .question import Question


class StudentAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_answer = models.TextField(null=True, blank=True)
    answered_at = models.DateTimeField(auto_now_add=True)
    student_test = models.ForeignKey(StudentTest, on_delete=models.CASCADE)
    is_correct = models.BooleanField(null=True)

    class Meta:
        unique_together = ['student_test', 'question']