from django.db import models
from exam_management.models import User


class Stream(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)

class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    stream = models.ForeignKey(Stream,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'stream')

class College(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    branch = models.ManyToManyField(Branch)
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE)


