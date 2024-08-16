from django.db import models
from .question import Question

class FillInTheBlankAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct_answer = models.TextField()