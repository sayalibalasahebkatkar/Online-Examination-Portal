from django.db import models
from .college import College, Branch,Stream

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    rollno = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=100)
    highestdegree = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    # resume = models.FileField(upload_to='resume/',blank=True,null=True)