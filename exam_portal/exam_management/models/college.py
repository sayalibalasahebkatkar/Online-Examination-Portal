from django.db import models
from .admin import Admin


class Stream(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    stream = models.ForeignKey(Stream)

class College(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    branch = models.ManyToManyField(Branch)
    registered_by = models.ForeignKey(Admin, on_delete=models.CASCADE)


