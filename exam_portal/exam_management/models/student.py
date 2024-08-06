from django.db import models
from exam_management.models import College, Branch,Stream
from django.contrib.auth.hashers import make_password

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    rollno = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=100,choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    highestdegree = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    college = models.ForeignKey(College, on_delete=models.CASCADE,null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,null=True, blank=True)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE,null=True, blank=True)
    # token = models.UUIDField(default=uuid.uuid4, editable=False)

    def save(self, *args, **kwargs):
        if self._state.adding and self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
