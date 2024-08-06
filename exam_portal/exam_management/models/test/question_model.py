from django.db import models
from .test_model import Test

class Question(models.Model):
    QUESTION_TYPES = [
        ('MCQ', 'MCQ'),
        ('FIB', 'FIB'),
        ('SQL', 'SQL'),
    ]
    id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=128)
    question_type = models.CharField(max_length=3, choices=QUESTION_TYPES)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['question_text', 'test']