from django.db import models

from .test import Test
from .question_tag import Tag

class Question(models.Model):
    QUESTION_TYPES = [
        ('MCQ', 'MCQ'),
        ('FIB', 'FIB'),
        ('SQL', 'SQL'),
    ]
    id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=128)
    question_type = models.CharField(max_length=3, choices=QUESTION_TYPES)
    tags = models.ManyToManyField(Tag, related_name='questions', blank=True)

    class Meta:
        unique_together = ('question_text', 'question_type')