from django.db import models

from .test import Test
from .question import Question

class TestQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # order = models.IntegerField(default=0)  # optional: to keep track of the order of questions in the test
    # marks = models.IntegerField(default=1)  # optional: to assign marks to the question for this test

    class Meta:
        unique_together = ['test', 'question']