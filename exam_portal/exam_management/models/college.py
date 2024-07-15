from django.db import models
from exam_management.models import User


class Stream(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    stream = models.ForeignKey(Stream,on_delete=models.CASCADE)

class College(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    branch = models.ManyToManyField(Branch)
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE)


