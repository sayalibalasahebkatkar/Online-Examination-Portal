from django.db import models
from .question import Question

class SqlQuery(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    expected_answer = models.TextField()